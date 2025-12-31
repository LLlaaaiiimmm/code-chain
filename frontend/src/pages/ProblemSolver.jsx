import { useState, useEffect } from "react";
import { useParams, Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import Editor from "@monaco-editor/react";
import { Button } from "../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../components/ui/tabs";
import { toast } from "sonner";
import {
  Boxes, Play, CheckCircle, XCircle, ChevronLeft,
  Clock, Zap, Lightbulb, Code2, Terminal, LogOut, User
} from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "../components/ui/dropdown-menu";
import { Avatar, AvatarFallback, AvatarImage } from "../components/ui/avatar";
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "../components/ui/resizable";
import { API } from "../App";

const ProblemSolver = ({ user, token, onLogout }) => {
  const { problemId } = useParams();
  const navigate = useNavigate();
  const [problem, setProblem] = useState(null);
  const [code, setCode] = useState("");
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState(null);
  const [showHints, setShowHints] = useState(false);
  const [isSolved, setIsSolved] = useState(false);
  const [solvedSubmission, setSolvedSubmission] = useState(null);

  useEffect(() => {
    fetchProblem();
    checkProblemStatus();
  }, [problemId]);

  const fetchProblem = async () => {
    try {
      const response = await axios.get(`${API}/problems/${problemId}`);
      setProblem(response.data);
      setCode(response.data.initial_code);
    } catch (error) {
      toast.error("Problem not found");
      navigate("/problems");
    } finally {
      setLoading(false);
    }
  };

  const checkProblemStatus = async () => {
    try {
      const response = await axios.get(
        `${API}/problems/${problemId}/status`,
        {
          headers: { Authorization: `Bearer ${token}` },
          withCredentials: true
        }
      );
      setIsSolved(response.data.is_solved);
      setSolvedSubmission(response.data.submission);
    } catch (error) {
      console.error("Failed to check problem status:", error);
    }
  };

  const handleSubmit = async () => {
    // Validate code is not empty
    const codeStripped = code.trim();
    if (!codeStripped || codeStripped.length < 10) {
      toast.error("Please write a meaningful solution (minimum 10 characters)");
      return;
    }

    // Check if problem is already solved
    if (isSolved) {
      toast.error("You have already solved this problem. Each problem can only be solved once.");
      return;
    }

    setSubmitting(true);
    setResult(null);

    try {
      const response = await axios.post(
        `${API}/submissions`,
        {
          problem_id: problemId,
          code: code,
          language: problem?.category || "solidity"
        },
        {
          headers: { Authorization: `Bearer ${token}` },
          withCredentials: true
        }
      );

      setResult(response.data);
      
      if (response.data.status === "passed") {
        toast.success(`All tests passed! +${response.data.elo_change} ELO`);
        setIsSolved(true);
        setSolvedSubmission(response.data);
      } else {
        toast.error("Some tests failed. Check the results below.");
      }
    } catch (error) {
      const errorMsg = error.response?.data?.detail || "Submission failed";
      toast.error(errorMsg);
    } finally {
      setSubmitting(false);
    }
  };

  const getDifficultyColor = (diff) => {
    const colors = {
      junior: "text-green-400 border-green-500/30 bg-green-500/10",
      middle: "text-yellow-400 border-yellow-500/30 bg-yellow-500/10",
      senior: "text-orange-400 border-orange-500/30 bg-orange-500/10",
      expert: "text-red-400 border-red-500/30 bg-red-500/10"
    };
    return colors[diff] || "";
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <div className="w-8 h-8 border-2 border-primary border-t-transparent rounded-full animate-spin"></div>
      </div>
    );
  }

  return (
    <div className="h-screen bg-background flex flex-col" data-testid="problem-solver-page">
      {/* Header */}
      <header className="h-14 border-b border-border flex items-center justify-between px-4 bg-card/50 shrink-0">
        <div className="flex items-center gap-4">
          <Link to="/problems">
            <Button variant="ghost" size="sm">
              <ChevronLeft className="w-4 h-4 mr-1" />
              Back
            </Button>
          </Link>
          <div className="flex items-center gap-2">
            <Boxes className="w-6 h-6 text-primary" />
            <span className="font-secondary font-bold">CodeChain</span>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <Badge className={`border ${getDifficultyColor(problem?.difficulty)}`}>
            {problem?.difficulty}
          </Badge>
          <Badge variant="outline">{problem?.category}</Badge>
          
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="ghost" size="sm">
                <Avatar className="w-6 h-6">
                  <AvatarImage src={user?.picture} />
                  <AvatarFallback className="bg-primary/20 text-primary text-xs">
                    {user?.name?.charAt(0)}
                  </AvatarFallback>
                </Avatar>
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end">
              <DropdownMenuItem asChild>
                <Link to="/profile"><User className="w-4 h-4 mr-2" />Profile</Link>
              </DropdownMenuItem>
              <DropdownMenuSeparator />
              <DropdownMenuItem onClick={onLogout} className="text-red-400">
                <LogOut className="w-4 h-4 mr-2" />Logout
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </header>

      {/* Main Content */}
      <div className="flex-1 overflow-hidden">
        <ResizablePanelGroup direction="horizontal">
          {/* Problem Description Panel */}
          <ResizablePanel defaultSize={35} minSize={25}>
            <div className="h-full overflow-auto p-6 bg-background">
              <motion.div
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.4 }}
              >
                <h1 className="font-secondary text-2xl font-bold mb-4 flex items-center gap-3">
                  {problem?.title}
                  {isSolved && (
                    <Badge className="bg-green-500/20 text-green-400 border-green-500/30">
                      <CheckCircle className="w-3 h-3 mr-1" />
                      Solved
                    </Badge>
                  )}
                </h1>
                
                <div className="flex items-center gap-4 mb-6 text-sm text-muted-foreground">
                  <span className="flex items-center gap-1">
                    <CheckCircle className="w-4 h-4 text-green-400" />
                    {problem?.solved_count || 0} solved
                  </span>
                  {isSolved && solvedSubmission && (
                    <span className="flex items-center gap-1 text-green-400">
                      <Zap className="w-4 h-4" />
                      You earned +{solvedSubmission.elo_change} ELO
                    </span>
                  )}
                </div>

                <div className="prose prose-invert prose-sm max-w-none mb-6">
                  <p className="text-zinc-300 leading-relaxed whitespace-pre-wrap">
                    {problem?.description}
                  </p>
                </div>

                {/* Tags */}
                {problem?.tags?.length > 0 && (
                  <div className="mb-6">
                    <h3 className="text-sm font-medium mb-2 text-muted-foreground">Tags</h3>
                    <div className="flex flex-wrap gap-2">
                      {problem.tags.map((tag, i) => (
                        <Badge key={i} variant="secondary">{tag}</Badge>
                      ))}
                    </div>
                  </div>
                )}

                {/* Hints */}
                {problem?.hints?.length > 0 && (
                  <div className="mb-6">
                    <Button
                      variant="outline"
                      size="sm"
                      onClick={() => setShowHints(!showHints)}
                      className="mb-3"
                    >
                      <Lightbulb className="w-4 h-4 mr-2" />
                      {showHints ? "Hide Hints" : "Show Hints"}
                    </Button>
                    
                    {showHints && (
                      <motion.div
                        initial={{ opacity: 0, height: 0 }}
                        animate={{ opacity: 1, height: "auto" }}
                        className="space-y-2"
                      >
                        {problem.hints.map((hint, i) => (
                          <div key={i} className="p-3 rounded-lg bg-yellow-500/10 border border-yellow-500/20">
                            <p className="text-sm text-yellow-200">{hint}</p>
                          </div>
                        ))}
                      </motion.div>
                    )}
                  </div>
                )}

                {/* Test Cases Preview */}
                <div>
                  <h3 className="text-sm font-medium mb-2 text-muted-foreground">Test Cases</h3>
                  <div className="space-y-2">
                    {problem?.test_cases?.slice(0, 2).map((test, i) => (
                      <div key={i} className="p-3 rounded-lg bg-secondary/50 font-mono text-xs">
                        <p className="text-muted-foreground">Input: <span className="text-foreground">{test.input}</span></p>
                        <p className="text-muted-foreground">Expected: <span className="text-green-400">{test.expected}</span></p>
                      </div>
                    ))}
                  </div>
                </div>
              </motion.div>
            </div>
          </ResizablePanel>

          <ResizableHandle withHandle />

          {/* Code Editor Panel */}
          <ResizablePanel defaultSize={40} minSize={30}>
            <div className="h-full flex flex-col">
              <div className="flex items-center justify-between px-4 py-2 bg-card border-b border-border">
                <div className="flex items-center gap-2">
                  <Code2 className="w-4 h-4 text-primary" />
                  <span className="text-sm font-mono">{problem?.category}.sol</span>
                </div>
                <Button
                  onClick={handleSubmit}
                  disabled={submitting}
                  className="glow-primary"
                  data-testid="submit-btn"
                >
                  {submitting ? (
                    <>
                      <div className="w-4 h-4 border-2 border-primary-foreground border-t-transparent rounded-full animate-spin mr-2" />
                      Running...
                    </>
                  ) : (
                    <>
                      <Play className="w-4 h-4 mr-2" />
                      Submit
                    </>
                  )}
                </Button>
              </div>
              
              <div className="flex-1">
                <Editor
                  height="100%"
                  language="sol"
                  theme="vs-dark"
                  value={code}
                  onChange={(value) => setCode(value || "")}
                  options={{
                    minimap: { enabled: false },
                    fontSize: 14,
                    fontFamily: "'JetBrains Mono', monospace",
                    lineNumbers: "on",
                    scrollBeyondLastLine: false,
                    automaticLayout: true,
                    tabSize: 4,
                    wordWrap: "on",
                    padding: { top: 16 }
                  }}
                />
              </div>
            </div>
          </ResizablePanel>

          <ResizableHandle withHandle />

          {/* Results Panel */}
          <ResizablePanel defaultSize={25} minSize={20}>
            <div className="h-full overflow-auto bg-background">
              <Tabs defaultValue="results" className="h-full flex flex-col">
                <TabsList className="w-full justify-start px-4 pt-2 bg-transparent">
                  <TabsTrigger value="results">
                    <Terminal className="w-4 h-4 mr-2" />
                    Results
                  </TabsTrigger>
                  <TabsTrigger value="console">Console</TabsTrigger>
                </TabsList>
                
                <TabsContent value="results" className="flex-1 p-4 mt-0">
                  {result ? (
                    <motion.div
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      className="space-y-4"
                    >
                      {/* Status Banner */}
                      <div className={`p-4 rounded-lg ${
                        result.status === "passed" 
                          ? "bg-green-500/10 border border-green-500/30" 
                          : "bg-red-500/10 border border-red-500/30"
                      }`}>
                        <div className="flex items-center gap-2 mb-2">
                          {result.status === "passed" ? (
                            <CheckCircle className="w-5 h-5 text-green-400" />
                          ) : (
                            <XCircle className="w-5 h-5 text-red-400" />
                          )}
                          <span className={`font-semibold ${
                            result.status === "passed" ? "text-green-400" : "text-red-400"
                          }`}>
                            {result.status === "passed" ? "All Tests Passed!" : "Tests Failed"}
                          </span>
                        </div>
                        {result.elo_change > 0 && (
                          <p className="text-sm text-green-400">+{result.elo_change} ELO</p>
                        )}
                      </div>

                      {/* Stats */}
                      <div className="grid grid-cols-2 gap-3">
                        <div className="p-3 rounded-lg bg-card border border-border">
                          <div className="flex items-center gap-2 text-muted-foreground text-xs mb-1">
                            <Zap className="w-3 h-3" />
                            Gas Used
                          </div>
                          <p className="font-mono text-sm">{result.gas_used?.toLocaleString()}</p>
                        </div>
                        <div className="p-3 rounded-lg bg-card border border-border">
                          <div className="flex items-center gap-2 text-muted-foreground text-xs mb-1">
                            <Clock className="w-3 h-3" />
                            Time
                          </div>
                          <p className="font-mono text-sm">{result.execution_time_ms}ms</p>
                        </div>
                      </div>

                      {/* Test Results */}
                      <div className="space-y-2">
                        <h4 className="text-sm font-medium text-muted-foreground">Test Cases</h4>
                        {result.test_results?.map((test, i) => (
                          <div 
                            key={i} 
                            className={`p-3 rounded-lg border ${
                              test.passed 
                                ? "bg-green-500/5 border-green-500/20" 
                                : "bg-red-500/5 border-red-500/20"
                            }`}
                          >
                            <div className="flex items-center gap-2 mb-1">
                              {test.passed ? (
                                <CheckCircle className="w-4 h-4 text-green-400" />
                              ) : (
                                <XCircle className="w-4 h-4 text-red-400" />
                              )}
                              <span className="text-sm font-medium">Test {test.test_id}</span>
                            </div>
                            <p className="text-xs font-mono text-muted-foreground">
                              Input: {test.input}
                            </p>
                            <p className="text-xs font-mono text-muted-foreground">
                              Expected: {test.expected}
                            </p>
                            {test.error && (
                              <p className="text-xs font-mono text-red-400 mt-1">
                                Error: {test.error}
                              </p>
                            )}
                          </div>
                        ))}
                      </div>
                    </motion.div>
                  ) : (
                    <div className="flex flex-col items-center justify-center h-full text-center">
                      <Terminal className="w-12 h-12 text-muted-foreground mb-4" />
                      <p className="text-muted-foreground">Submit your code to see results</p>
                    </div>
                  )}
                </TabsContent>
                
                <TabsContent value="console" className="flex-1 p-4 mt-0">
                  <div className="h-full rounded-lg bg-card border border-border p-4 font-mono text-sm">
                    <p className="text-muted-foreground">Console output will appear here...</p>
                  </div>
                </TabsContent>
              </Tabs>
            </div>
          </ResizablePanel>
        </ResizablePanelGroup>
      </div>
    </div>
  );
};

export default ProblemSolver;
