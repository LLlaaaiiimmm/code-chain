import { useState, useEffect } from "react";
import { Link, useSearchParams } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";
import { Card, CardContent } from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../components/ui/select";
import { 
  Boxes, Search, Filter, Code2, CheckCircle, 
  ChevronRight, Users, Trophy, LogOut, User
} from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "../components/ui/dropdown-menu";
import { Avatar, AvatarFallback, AvatarImage } from "../components/ui/avatar";
import { API } from "../App";

const Problems = ({ user, token, onLogout }) => {
  const [searchParams, setSearchParams] = useSearchParams();
  const [problems, setProblems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [total, setTotal] = useState(0);
  const [search, setSearch] = useState(searchParams.get("search") || "");
  const [difficulty, setDifficulty] = useState(searchParams.get("difficulty") || "all");
  const [category, setCategory] = useState(searchParams.get("category") || "all");
  const [solvedProblems, setSolvedProblems] = useState(new Set());

  useEffect(() => {
    fetchProblems();
    fetchSolvedProblems();
  }, [difficulty, category]);

  const fetchProblems = async () => {
    setLoading(true);
    try {
      const params = new URLSearchParams();
      if (difficulty && difficulty !== "all") params.append("difficulty", difficulty);
      if (category && category !== "all") params.append("category", category);
      if (search) params.append("search", search);

      const response = await axios.get(`${API}/problems?${params.toString()}`);
      // Filter out problems with 0 solved count
      const filteredProblems = response.data.problems.filter(p => p.solved_count > 0);
      setProblems(filteredProblems);
      setTotal(filteredProblems.length);
    } catch (error) {
      console.error("Error fetching problems:", error);
    } finally {
      setLoading(false);
    }
  };

  const fetchSolvedProblems = async () => {
    try {
      const response = await axios.get(
        `${API}/submissions`,
        {
          headers: { Authorization: `Bearer ${token}` },
          withCredentials: true
        }
      );
      const solved = new Set(
        response.data
          .filter(sub => sub.status === "passed")
          .map(sub => sub.problem_id)
      );
      setSolvedProblems(solved);
    } catch (error) {
      console.error("Error fetching solved problems:", error);
    }
  };

  const handleSearch = (e) => {
    e.preventDefault();
    fetchProblems();
  };

  const getDifficultyBadge = (diff) => {
    const styles = {
      junior: "difficulty-junior",
      middle: "difficulty-middle",
      senior: "difficulty-senior",
      expert: "difficulty-expert"
    };
    return styles[diff] || "";
  };

  const getCategoryBadge = (cat) => {
    const styles = {
      solidity: "category-solidity",
      rust: "category-rust",
      move: "category-move",
      tvm: "category-tvm"
    };
    return styles[cat] || "";
  };

  return (
    <div className="min-h-screen bg-background" data-testid="problems-page">
      {/* Navigation */}
      <nav className="sticky top-0 z-50 glass border-b border-border">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center gap-8">
              <Link to="/" className="flex items-center gap-2">
                <Boxes className="w-8 h-8 text-primary" />
                <span className="font-secondary text-xl font-bold">CodeChain</span>
              </Link>
              
              <div className="hidden md:flex items-center gap-6">
                <Link to="/dashboard" className="text-muted-foreground hover:text-foreground transition-colors">Dashboard</Link>
                <Link to="/problems" className="text-foreground font-medium">Problems</Link>
                <Link to="/leaderboard" className="text-muted-foreground hover:text-foreground transition-colors">Leaderboard</Link>
                <Link to="/hackathons" className="text-muted-foreground hover:text-foreground transition-colors">Hackathons</Link>
              </div>
            </div>

            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button variant="ghost" className="flex items-center gap-2">
                  <Avatar className="w-8 h-8">
                    <AvatarImage src={user?.picture} />
                    <AvatarFallback className="bg-primary/20 text-primary">
                      {user?.name?.charAt(0) || "U"}
                    </AvatarFallback>
                  </Avatar>
                  <span className="hidden md:inline">{user?.name}</span>
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="end" className="w-56">
                <DropdownMenuItem asChild>
                  <Link to="/profile" className="flex items-center gap-2">
                    <User className="w-4 h-4" />
                    Profile
                  </Link>
                </DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem onClick={onLogout} className="text-red-400">
                  <LogOut className="w-4 h-4 mr-2" />
                  Logout
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4 }}
        >
          {/* Header */}
          <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-8">
            <div>
              <h1 className="font-secondary text-3xl font-bold mb-1">Problem Library</h1>
              <p className="text-muted-foreground">{total} challenges available</p>
            </div>
          </div>

          {/* Filters */}
          <div className="flex flex-col md:flex-row gap-4 mb-8">
            <form onSubmit={handleSearch} className="flex-1">
              <div className="relative">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
                <Input
                  placeholder="Search problems..."
                  className="pl-10"
                  value={search}
                  onChange={(e) => setSearch(e.target.value)}
                  data-testid="search-input"
                />
              </div>
            </form>

            <div className="flex gap-3">
              <Select value={difficulty} onValueChange={setDifficulty}>
                <SelectTrigger className="w-[140px]" data-testid="difficulty-filter">
                  <SelectValue placeholder="Difficulty" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="all">All Levels</SelectItem>
                  <SelectItem value="junior">Junior</SelectItem>
                  <SelectItem value="middle">Middle</SelectItem>
                  <SelectItem value="senior">Senior</SelectItem>
                  <SelectItem value="expert">Expert</SelectItem>
                </SelectContent>
              </Select>

              <Select value={category} onValueChange={setCategory}>
                <SelectTrigger className="w-[140px]" data-testid="category-filter">
                  <SelectValue placeholder="Category" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="all">All Categories</SelectItem>
                  <SelectItem value="solidity">Solidity</SelectItem>
                  <SelectItem value="rust">Rust</SelectItem>
                  <SelectItem value="move">Move</SelectItem>
                  <SelectItem value="tvm">TVM</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>

          {/* Problems List */}
          {loading ? (
            <div className="grid gap-4">
              {[...Array(5)].map((_, i) => (
                <div key={i} className="h-24 bg-card rounded-lg animate-pulse" />
              ))}
            </div>
          ) : problems.length > 0 ? (
            <div className="space-y-4">
              {problems.map((problem, i) => (
                <motion.div
                  key={problem.problem_id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.3, delay: i * 0.05 }}
                >
                  <Link to={`/problems/${problem.problem_id}`}>
                    <Card 
                      className="bg-card border-border hover:border-primary/50 transition-all duration-300 cursor-pointer group"
                      data-testid={`problem-card-${problem.problem_id}`}
                    >
                      <CardContent className="p-6">
                        <div className="flex items-start justify-between gap-4">
                          <div className="flex-1">
                            <div className="flex items-center gap-3 mb-2">
                              <h3 className="font-secondary text-lg font-semibold group-hover:text-primary transition-colors">
                                {problem.title}
                              </h3>
                              <Badge className={`border ${getDifficultyBadge(problem.difficulty)}`}>
                                {problem.difficulty}
                              </Badge>
                              <Badge className={`border ${getCategoryBadge(problem.category)}`}>
                                {problem.category}
                              </Badge>
                              {solvedProblems.has(problem.problem_id) && (
                                <Badge className="bg-green-500/20 text-green-400 border-green-500/30">
                                  <CheckCircle className="w-3 h-3 mr-1" />
                                  Solved
                                </Badge>
                              )}
                            </div>
                            <p className="text-muted-foreground text-sm line-clamp-2 mb-3">
                              {problem.description}
                            </p>
                            <div className="flex items-center gap-4 text-sm text-muted-foreground">
                              <span className="flex items-center gap-1">
                                <Users className="w-4 h-4" />
                                {problem.solved_count || 0} solved
                              </span>
                              {problem.tags?.length > 0 && (
                                <span className="flex items-center gap-2">
                                  {problem.tags.slice(0, 3).map((tag, j) => (
                                    <span key={j} className="px-2 py-0.5 rounded bg-secondary text-xs">
                                      {tag}
                                    </span>
                                  ))}
                                </span>
                              )}
                            </div>
                          </div>
                          <ChevronRight className="w-5 h-5 text-muted-foreground group-hover:text-primary transition-colors" />
                        </div>
                      </CardContent>
                    </Card>
                  </Link>
                </motion.div>
              ))}
            </div>
          ) : (
            <Card className="bg-card border-border">
              <CardContent className="py-12 text-center">
                <Code2 className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
                <h3 className="font-secondary text-xl font-semibold mb-2">No problems found</h3>
                <p className="text-muted-foreground mb-4">Try adjusting your filters or search query</p>
                <Button 
                  variant="outline" 
                  onClick={() => {
                    setSearch("");
                    setDifficulty("all");
                    setCategory("all");
                  }}
                >
                  Clear Filters
                </Button>
              </CardContent>
            </Card>
          )}
        </motion.div>
      </main>
    </div>
  );
};

export default Problems;
