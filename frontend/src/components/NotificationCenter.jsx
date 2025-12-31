import { useState, useEffect } from "react";
import axios from "axios";
import { motion, AnimatePresence } from "framer-motion";
import { Button } from "./ui/button";
import { Badge } from "./ui/badge";
import { ScrollArea } from "./ui/scroll-area";
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "./ui/sheet";
import { 
  Bell, Trophy, Target, TrendingUp, Flame, 
  AlertCircle, CheckCircle, X
} from "lucide-react";
import { API } from "../App";

export const NotificationCenter = ({ token }) => {
  const [notifications, setNotifications] = useState([]);
  const [unreadCount, setUnreadCount] = useState(0);
  const [loading, setLoading] = useState(false);
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    if (isOpen) {
      fetchNotifications();
    } else {
      // Just fetch unread count when closed
      fetchUnreadCount();
    }
  }, [isOpen]);

  const fetchUnreadCount = async () => {
    try {
      const response = await axios.get(`${API}/notifications?unread_only=true&limit=1`, {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true
      });
      setUnreadCount(response.data.unread_count || 0);
    } catch (error) {
      console.error("Error fetching unread count:", error);
    }
  };

  const fetchNotifications = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${API}/notifications?limit=50`, {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true
      });
      setNotifications(response.data.notifications || []);
      setUnreadCount(response.data.unread_count || 0);
    } catch (error) {
      console.error("Error fetching notifications:", error);
    } finally {
      setLoading(false);
    }
  };

  const markAsRead = async (notificationId) => {
    try {
      await axios.post(
        `${API}/notifications/${notificationId}/read`,
        {},
        {
          headers: { Authorization: `Bearer ${token}` },
          withCredentials: true
        }
      );
      // Update local state
      setNotifications(notifications.map(n => 
        n.notification_id === notificationId ? { ...n, read: true } : n
      ));
      setUnreadCount(Math.max(0, unreadCount - 1));
    } catch (error) {
      console.error("Error marking notification as read:", error);
    }
  };

  const markAllAsRead = async () => {
    try {
      await axios.post(
        `${API}/notifications/mark-all-read`,
        {},
        {
          headers: { Authorization: `Bearer ${token}` },
          withCredentials: true
        }
      );
      // Update local state
      setNotifications(notifications.map(n => ({ ...n, read: true })));
      setUnreadCount(0);
    } catch (error) {
      console.error("Error marking all as read:", error);
    }
  };

  const getNotificationIcon = (type) => {
    switch (type) {
      case "achievement":
        return <Trophy className="w-5 h-5 text-yellow-400" />;
      case "milestone":
        return <Target className="w-5 h-5 text-purple-400" />;
      case "reminder":
        return <AlertCircle className="w-5 h-5 text-blue-400" />;
      case "challenge":
        return <Flame className="w-5 h-5 text-orange-400" />;
      case "rank_up":
        return <TrendingUp className="w-5 h-5 text-green-400" />;
      default:
        return <Bell className="w-5 h-5 text-muted-foreground" />;
    }
  };

  const getNotificationBg = (type) => {
    switch (type) {
      case "achievement":
        return "bg-yellow-500/10 border-yellow-500/30";
      case "milestone":
        return "bg-purple-500/10 border-purple-500/30";
      case "reminder":
        return "bg-blue-500/10 border-blue-500/30";
      case "challenge":
        return "bg-orange-500/10 border-orange-500/30";
      case "rank_up":
        return "bg-green-500/10 border-green-500/30";
      default:
        return "bg-secondary/30 border-border";
    }
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    const now = new Date();
    const diffMs = now - date;
    const diffMins = Math.floor(diffMs / 60000);
    const diffHours = Math.floor(diffMs / 3600000);
    const diffDays = Math.floor(diffMs / 86400000);

    if (diffMins < 1) return "Just now";
    if (diffMins < 60) return `${diffMins}m ago`;
    if (diffHours < 24) return `${diffHours}h ago`;
    if (diffDays < 7) return `${diffDays}d ago`;
    return date.toLocaleDateString();
  };

  return (
    <Sheet open={isOpen} onOpenChange={setIsOpen}>
      <SheetTrigger asChild>
        <Button 
          variant="ghost" 
          size="icon" 
          className="relative"
          data-testid="notifications-btn"
        >
          <Bell className="w-5 h-5" />
          {unreadCount > 0 && (
            <motion.span
              initial={{ scale: 0 }}
              animate={{ scale: 1 }}
              className="absolute -top-1 -right-1 flex items-center justify-center w-5 h-5 text-xs font-bold text-white bg-red-500 rounded-full"
            >
              {unreadCount > 9 ? "9+" : unreadCount}
            </motion.span>
          )}
        </Button>
      </SheetTrigger>
      
      <SheetContent className="w-full sm:max-w-md">
        <SheetHeader>
          <div className="flex items-center justify-between">
            <SheetTitle className="font-secondary text-xl flex items-center gap-2">
              <Bell className="w-5 h-5" />
              Notifications
            </SheetTitle>
            {unreadCount > 0 && (
              <Button 
                variant="ghost" 
                size="sm"
                onClick={markAllAsRead}
                className="text-xs"
              >
                Mark all read
              </Button>
            )}
          </div>
          <SheetDescription>
            Stay updated with your progress and achievements
          </SheetDescription>
        </SheetHeader>
        
        <ScrollArea className="h-[calc(100vh-120px)] mt-6 pr-4">
          {loading ? (
            <div className="space-y-3">
              {[1, 2, 3, 4].map((i) => (
                <div key={i} className="h-24 bg-secondary/50 rounded-lg animate-pulse" />
              ))}
            </div>
          ) : notifications.length > 0 ? (
            <div className="space-y-3">
              <AnimatePresence>
                {notifications.map((notification, index) => (
                  <motion.div
                    key={notification.notification_id}
                    initial={{ opacity: 0, x: 20 }}
                    animate={{ opacity: 1, x: 0 }}
                    exit={{ opacity: 0, x: -20 }}
                    transition={{ delay: index * 0.05 }}
                    className={`p-4 rounded-lg border ${getNotificationBg(notification.type)} ${
                      !notification.read ? 'border-l-4' : ''
                    } relative group`}
                  >
                    {!notification.read && (
                      <Button
                        variant="ghost"
                        size="icon"
                        className="absolute top-2 right-2 opacity-0 group-hover:opacity-100 transition-opacity h-6 w-6"
                        onClick={() => markAsRead(notification.notification_id)}
                      >
                        <CheckCircle className="w-4 h-4" />
                      </Button>
                    )}
                    
                    <div className="flex items-start gap-3">
                      <div className="mt-0.5">
                        {getNotificationIcon(notification.type)}
                      </div>
                      
                      <div className="flex-1 min-w-0 pr-6">
                        <div className="flex items-start justify-between gap-2 mb-1">
                          <h4 className="font-semibold text-sm">
                            {notification.title}
                          </h4>
                          {!notification.read && (
                            <Badge 
                              variant="outline" 
                              className="bg-primary/20 text-primary border-primary/30 text-xs shrink-0"
                            >
                              New
                            </Badge>
                          )}
                        </div>
                        
                        <p className="text-xs text-muted-foreground mb-2">
                          {notification.message}
                        </p>
                        
                        <span className="text-xs text-muted-foreground">
                          {formatDate(notification.created_at)}
                        </span>
                      </div>
                    </div>
                  </motion.div>
                ))}
              </AnimatePresence>
            </div>
          ) : (
            <div className="flex flex-col items-center justify-center h-64 text-center">
              <Bell className="w-16 h-16 text-muted-foreground mb-4" />
              <p className="text-sm text-muted-foreground">
                No notifications yet
              </p>
              <p className="text-xs text-muted-foreground mt-1">
                Keep solving to earn achievements and milestones!
              </p>
            </div>
          )}
        </ScrollArea>
      </SheetContent>
    </Sheet>
  );
};
