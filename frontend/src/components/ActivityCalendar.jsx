import CalendarHeatmap from 'react-calendar-heatmap';
import 'react-calendar-heatmap/dist/styles.css';
import { Tooltip } from './ui/tooltip';
import { TooltipContent, TooltipProvider, TooltipTrigger } from './ui/tooltip';

export const ActivityCalendar = ({ activities = [] }) => {
  // Calculate date range (last 365 days)
  const endDate = new Date();
  const startDate = new Date();
  startDate.setDate(startDate.getDate() - 365);

  // Transform activities data for heatmap
  const activityData = activities.map(activity => ({
    date: activity.date,
    count: activity.problems_solved
  }));

  const getColor = (value) => {
    if (!value || value.count === 0) return 'fill-zinc-800';
    if (value.count >= 5) return 'fill-green-500';
    if (value.count >= 3) return 'fill-green-400';
    if (value.count >= 2) return 'fill-green-300';
    return 'fill-green-200';
  };

  return (
    <div className="w-full">
      <style>{`
        .react-calendar-heatmap .color-empty { fill: #27272a; }
        .react-calendar-heatmap .color-scale-1 { fill: #bbf7d0; }
        .react-calendar-heatmap .color-scale-2 { fill: #86efac; }
        .react-calendar-heatmap .color-scale-3 { fill: #4ade80; }
        .react-calendar-heatmap .color-scale-4 { fill: #22c55e; }
        .react-calendar-heatmap text { fill: #a1a1aa; font-size: 10px; }
        .react-calendar-heatmap rect { rx: 2; }
        .react-calendar-heatmap rect:hover { stroke: #22c55e; stroke-width: 1; }
      `}</style>
      
      <CalendarHeatmap
        startDate={startDate}
        endDate={endDate}
        values={activityData}
        classForValue={getColor}
        tooltipDataAttrs={(value) => {
          if (!value || !value.date) {
            return { 'data-tip': 'No activity' };
          }
          return {
            'data-tip': `${value.count} problems solved on ${new Date(value.date).toLocaleDateString()}`
          };
        }}
        showWeekdayLabels
      />
      
      <div className="flex items-center gap-2 mt-4 text-xs text-muted-foreground">
        <span>Less</span>
        <div className="flex gap-1">
          <div className="w-3 h-3 bg-zinc-800 rounded" />
          <div className="w-3 h-3 bg-green-200 rounded" />
          <div className="w-3 h-3 bg-green-300 rounded" />
          <div className="w-3 h-3 bg-green-400 rounded" />
          <div className="w-3 h-3 bg-green-500 rounded" />
        </div>
        <span>More</span>
      </div>
    </div>
  );
};
