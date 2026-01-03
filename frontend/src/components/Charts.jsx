import { LineChart, Line, AreaChart, Area, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

export const ELOProgressChart = ({ data = [] }) => {
  return (
    <ResponsiveContainer width="100%" height={300}>
      <AreaChart data={data}>
        <defs>
          <linearGradient id="colorElo" x1="0" y1="0" x2="0" y2="1">
            <stop offset="5%" stopColor="#a855f7" stopOpacity={0.8}/>
            <stop offset="95%" stopColor="#a855f7" stopOpacity={0}/>
          </linearGradient>
        </defs>
        <CartesianGrid strokeDasharray="3 3" stroke="#3f3f46" />
        <XAxis 
          dataKey="date" 
          stroke="#a1a1aa"
          fontSize={12}
          tickFormatter={(value) => {
            const date = new Date(value);
            return `${date.getMonth() + 1}/${date.getDate()}`;
          }}
        />
        <YAxis stroke="#a1a1aa" fontSize={12} />
        <Tooltip 
          contentStyle={{ 
            backgroundColor: '#18181b', 
            border: '1px solid #3f3f46',
            borderRadius: '6px'
          }}
          labelStyle={{ color: '#a1a1aa' }}
        />
        <Area 
          type="monotone" 
          dataKey="elo" 
          stroke="#a855f7" 
          fillOpacity={1}
          fill="url(#colorElo)"
        />
      </AreaChart>
    </ResponsiveContainer>
  );
};

export const ProblemDistributionChart = ({ data = {} }) => {
  const chartData = [
    { name: 'Junior', value: data.junior || 0, fill: '#22c55e' },
    { name: 'Middle', value: data.middle || 0, fill: '#eab308' },
    { name: 'Senior', value: data.senior || 0, fill: '#f97316' },
    { name: 'Expert', value: data.expert || 0, fill: '#ef4444' }
  ];

  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={chartData}>
        <CartesianGrid strokeDasharray="3 3" stroke="#3f3f46" />
        <XAxis dataKey="name" stroke="#a1a1aa" fontSize={12} />
        <YAxis stroke="#a1a1aa" fontSize={12} />
        <Tooltip 
          contentStyle={{ 
            backgroundColor: '#18181b', 
            border: '1px solid #3f3f46',
            borderRadius: '6px',
            color: '#ffffff'
          }}
          labelStyle={{ color: '#ffffff' }}
          itemStyle={{ color: '#ffffff' }}
        />
        <Bar dataKey="value" radius={[4, 4, 0, 0]} />
      </BarChart>
    </ResponsiveContainer>
  );
};

export const CategoryDistributionChart = ({ data = {} }) => {
  const chartData = [
    { name: 'Solidity', value: data.solidity || 0, fill: '#a855f7' },
    { name: 'Rust', value: data.rust || 0, fill: '#f97316' },
    { name: 'TVM', value: data.tvm || 0, fill: '#3b82f6' },
    { name: 'Crypto', value: data.crypto || 0, fill: '#eab308' }
  ];

  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={chartData} layout="vertical">
        <CartesianGrid strokeDasharray="3 3" stroke="#3f3f46" />
        <XAxis type="number" stroke="#a1a1aa" fontSize={12} />
        <YAxis dataKey="name" type="category" stroke="#a1a1aa" fontSize={12} />
        <Tooltip 
          contentStyle={{ 
            backgroundColor: '#18181b', 
            border: '1px solid #3f3f46',
            borderRadius: '6px',
            color: '#ffffff'
          }}
          labelStyle={{ color: '#ffffff' }}
          itemStyle={{ color: '#ffffff' }}
        />
        <Bar dataKey="value" radius={[0, 4, 4, 0]} />
      </BarChart>
    </ResponsiveContainer>
  );
};
