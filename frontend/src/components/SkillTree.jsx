import { useEffect, useState } from 'react';
import ReactFlow, { 
  Background, 
  Controls, 
  MiniMap,
  useNodesState,
  useEdgesState 
} from 'reactflow';
import 'reactflow/dist/style.css';
import { Badge } from './ui/badge';

const SkillNode = ({ data }) => {
  const getProgressColor = (progress) => {
    if (progress === 100) return 'bg-green-500';
    if (progress >= 50) return 'bg-yellow-500';
    if (progress > 0) return 'bg-blue-500';
    return 'bg-zinc-700';
  };

  const getCategoryColor = (category) => {
    const colors = {
      solidity: 'border-purple-500',
      rust: 'border-orange-500',
      tvm: 'border-blue-500',
      general: 'border-zinc-500'
    };
    return colors[category] || 'border-zinc-500';
  };

  return (
    <div 
      className={`px-4 py-3 rounded-lg border-2 ${getCategoryColor(data.category)} 
        ${data.unlocked ? 'bg-card' : 'bg-card/50 opacity-60'}
        shadow-lg min-w-[180px]`}
    >
      <div className="flex items-center justify-between mb-2">
        <span className="font-medium text-sm">{data.name}</span>
        {data.unlocked && <span className="text-green-400 text-xs">✓</span>}
      </div>
      
      <p className="text-xs text-muted-foreground mb-2 line-clamp-2">
        {data.description}
      </p>
      
      <div className="flex items-center gap-2">
        <div className="flex-1 h-1.5 bg-secondary rounded-full overflow-hidden">
          <div 
            className={`h-full ${getProgressColor(data.progress)} transition-all`}
            style={{ width: `${data.progress}%` }}
          />
        </div>
        <span className="text-xs text-muted-foreground">{data.progress}%</span>
      </div>
      
      <Badge variant="outline" className="mt-2 text-xs">
        Level {data.level}
      </Badge>
    </div>
  );
};

const nodeTypes = {
  skillNode: SkillNode
};

export const SkillTree = ({ skills = [] }) => {
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);

  useEffect(() => {
    if (!skills.length) return;

    // Group skills by category
    const categories = ['solidity', 'rust', 'tvm', 'general'];
    const categoryGroups = {};
    
    skills.forEach(skill => {
      if (!categoryGroups[skill.category]) {
        categoryGroups[skill.category] = [];
      }
      categoryGroups[skill.category].push(skill);
    });

    // Create nodes with layout
    const newNodes = [];
    let yOffset = 0;
    const categorySpacing = 200;
    const nodeSpacing = 250;

    Object.keys(categoryGroups).forEach(category => {
      const categorySkills = categoryGroups[category];
      
      categorySkills.forEach((skill, index) => {
        newNodes.push({
          id: skill.skill_id,
          type: 'skillNode',
          position: { 
            x: index * nodeSpacing, 
            y: yOffset 
          },
          data: skill
        });
      });
      
      yOffset += categorySpacing;
    });

    // Create edges based on dependencies
    const newEdges = [];
    skills.forEach(skill => {
      if (skill.dependencies && skill.dependencies.length > 0) {
        skill.dependencies.forEach(depId => {
          newEdges.push({
            id: `${depId}-${skill.skill_id}`,
            source: depId,
            target: skill.skill_id,
            type: 'smoothstep',
            animated: !skill.unlocked,
            style: { 
              stroke: skill.unlocked ? '#22c55e' : '#52525b',
              strokeWidth: 2
            }
          });
        });
      }
    });

    setNodes(newNodes);
    setEdges(newEdges);
  }, [skills, setNodes, setEdges]);

  if (!skills.length) {
    return (
      <div className="h-[400px] flex items-center justify-center text-muted-foreground">
        No skills data available
      </div>
    );
  }

  return (
    <div className="h-[600px] w-full rounded-lg border border-border bg-background">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        nodeTypes={nodeTypes}
        fitView
        minZoom={0.5}
        maxZoom={1.5}
      >
        <Background color="#52525b" gap={16} />
        <Controls className="bg-card border border-border" />
        <MiniMap 
          className="bg-card border border-border"
          nodeColor={(node) => {
            if (node.data.unlocked) return '#22c55e';
            return '#52525b';
          }}
        />
      </ReactFlow>
    </div>
  );
};
