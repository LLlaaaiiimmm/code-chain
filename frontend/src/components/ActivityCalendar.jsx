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
    if (!value || value.count === 0) return 'fill-zinc-800/50';
    if (value.count >= 5) return 'fill-emerald-500';
    if (value.count >= 3) return 'fill-emerald-400';
    if (value.count >= 2) return 'fill-emerald-300';
    return 'fill-emerald-200';
  };

  // Calculate statistics
  const totalSolved = activityData.reduce((acc, day) => acc + (day.count || 0), 0);
  const activeDays = activityData.filter(day => day.count > 0).length;
  const maxDay = activityData.reduce((max, day) => 
    day.count > (max?.count || 0) ? day : max, activityData[0]
  );

  return (
    <div className="w-full">
      <style>{`
        .react-calendar-heatmap {
          padding: 1rem 0;
        }
        .react-calendar-heatmap .color-empty { 
          fill: rgba(39, 39, 42, 0.5);
          stroke: rgba(63, 63, 70, 0.3);
          stroke-width: 1;
        }
        .react-calendar-heatmap .color-scale-1 { 
          fill: #bbf7d0; 
          stroke: #86efac;
          stroke-width: 1;
        }
        .react-calendar-heatmap .color-scale-2 { 
          fill: #86efac;
          stroke: #4ade80;
          stroke-width: 1;
        }
        .react-calendar-heatmap .color-scale-3 { 
          fill: #4ade80;
          stroke: #22c55e;
          stroke-width: 1;
        }
        .react-calendar-heatmap .color-scale-4 { 
          fill: #22c55e;
          stroke: #16a34a;
          stroke-width: 1;
        }
        .react-calendar-heatmap text { 
          fill: #a1a1aa; 
          font-size: 10px;
          font-weight: 500;
        }
        .react-calendar-heatmap rect { 
          rx: 3;
          transition: all 0.2s ease;
        }
        .react-calendar-heatmap rect:hover { 
          stroke: #10b981; 
          stroke-width: 2;
          transform: scale(1.1);
          filter: brightness(1.2);
        }
      `}</style>
      
      <div className="bg-zinc-900/50 rounded-xl p-6 border border-zinc-800">
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
              'data-tip': `${value.count} ${value.count === 1 ? 'problem' : 'problems'} solved on ${new Date(value.date).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}`
            };
          }}
          showWeekdayLabels
        />
        
        {/* Enhanced Legend */}
        <div className="flex items-center justify-between mt-6 pt-4 border-t border-zinc-800">
          <div className="flex items-center gap-3">
            <span className="text-xs text-muted-foreground font-medium">Less</span>
            <div className="flex gap-1.5">
              <div className="w-4 h-4 bg-zinc-800/50 rounded border border-zinc-700 hover:scale-110 transition-transform" />
              <div className="w-4 h-4 bg-emerald-200 rounded border border-emerald-300 hover:scale-110 transition-transform" />
              <div className="w-4 h-4 bg-emerald-300 rounded border border-emerald-400 hover:scale-110 transition-transform" />
              <div className="w-4 h-4 bg-emerald-400 rounded border border-emerald-500 hover:scale-110 transition-transform" />
              <div className="w-4 h-4 bg-emerald-500 rounded border border-emerald-600 hover:scale-110 transition-transform" />
            </div>
            <span className="text-xs text-muted-foreground font-medium">More</span>
          </div>
          
          {/* Activity Stats */}
          <div className="flex items-center gap-6 text-xs">
            <div className="flex items-center gap-2">
              <span className="text-muted-foreground">Total:</span>
              <span className="font-bold text-emerald-400">{totalSolved}</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-muted-foreground">Active Days:</span>
              <span className="font-bold text-blue-400">{activeDays}</span>
            </div>
            {maxDay && maxDay.count > 0 && (
              <div className="flex items-center gap-2">
                <span className="text-muted-foreground">Best Day:</span>
                <span className="font-bold text-purple-400">{maxDay.count}</span>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
