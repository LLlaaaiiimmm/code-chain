import { Link } from "react-router-dom";
import { motion } from "framer-motion";
import { Button } from "../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import {
  Boxes, Check, X, Zap, Trophy, Users,
  Code2, Shield, Award, ChevronRight
} from "lucide-react";

const Pricing = ({ user }) => {
  const plans = [
    {
      name: "Basic",
      price: "Free",
      period: "",
      description: "Perfect for getting started",
      features: [
        { text: "10 problems per month", included: true },
        { text: "Basic leaderboard access", included: true },
        { text: "Community forums", included: true },
        { text: "Junior-level problems", included: true },
        { text: "Advanced problems", included: false },
        { text: "Detailed analytics", included: false },
        { text: "Priority support", included: false },
        { text: "NFT certificates", included: false },
      ],
      cta: "Get Started",
      popular: false,
      color: "border-border"
    },
    {
      name: "Pro",
      price: "$29",
      period: "/month",
      description: "For serious developers",
      features: [
        { text: "Unlimited problems", included: true },
        { text: "Full leaderboard access", included: true },
        { text: "All difficulty levels", included: true },
        { text: "Detailed analytics", included: true },
        { text: "Private competitions", included: true },
        { text: "Code review hints", included: true },
        { text: "Priority support", included: false },
        { text: "NFT certificates", included: false },
      ],
      cta: "Upgrade to Pro",
      popular: true,
      color: "border-primary"
    },
    {
      name: "Expert",
      price: "$99",
      period: "/month",
      description: "For elite professionals",
      features: [
        { text: "Everything in Pro", included: true },
        { text: "1-on-1 mentoring sessions", included: true },
        { text: "NFT skill certificates", included: true },
        { text: "Priority support 24/7", included: true },
        { text: "Early access to features", included: true },
        { text: "Recruiter visibility", included: true },
        { text: "Custom challenges", included: true },
        { text: "API access", included: true },
      ],
      cta: "Go Expert",
      popular: false,
      color: "border-purple-500"
    }
  ];

  const faqs = [
    {
      q: "Can I cancel anytime?",
      a: "Yes, you can cancel your subscription at any time. You'll continue to have access until the end of your billing period."
    },
    {
      q: "What payment methods do you accept?",
      a: "We accept all major credit cards, PayPal, and crypto payments (ETH, USDC, DAI)."
    },
    {
      q: "Do you offer team plans?",
      a: "Yes! Contact us for custom B2B pricing for teams and organizations."
    },
    {
      q: "What are NFT certificates?",
      a: "NFT certificates are verifiable on-chain credentials that prove your skills and achievements on the platform."
    }
  ];

  return (
    <div className="min-h-screen bg-background" data-testid="pricing-page">
      {/* Navigation */}
      <nav className="sticky top-0 z-50 glass border-b border-border">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <Link to="/" className="flex items-center gap-2">
              <Boxes className="w-8 h-8 text-primary" />
              <span className="font-secondary text-xl font-bold">CodeChain</span>
            </Link>
            
            <div className="hidden md:flex items-center gap-8">
              <Link to="/problems" className="text-muted-foreground hover:text-foreground transition-colors">Problems</Link>
              <Link to="/leaderboard" className="text-muted-foreground hover:text-foreground transition-colors">Leaderboard</Link>
              <Link to="/hackathons" className="text-muted-foreground hover:text-foreground transition-colors">Hackathons</Link>
              <Link to="/pricing" className="text-foreground font-medium">Pricing</Link>
            </div>

            {user ? (
              <Link to="/dashboard">
                <Button className="glow-primary">Dashboard</Button>
              </Link>
            ) : (
              <div className="flex items-center gap-3">
                <Link to="/login">
                  <Button variant="ghost">Login</Button>
                </Link>
                <Link to="/register">
                  <Button className="glow-primary">Get Started</Button>
                </Link>
              </div>
            )}
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4 }}
        >
          {/* Header */}
          <div className="text-center mb-16">
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 border border-primary/20 mb-6">
              <Award className="w-4 h-4 text-primary" />
              <span className="text-sm text-primary font-medium">Simple Pricing</span>
            </div>
            <h1 className="font-secondary text-4xl md:text-5xl font-bold mb-4">
              Choose Your Path
            </h1>
            <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
              Start free and scale as you grow. No hidden fees, no surprises.
            </p>
          </div>

          {/* Pricing Cards */}
          <div className="grid md:grid-cols-3 gap-8 mb-20">
            {plans.map((plan, i) => (
              <motion.div
                key={plan.name}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.4, delay: i * 0.1 }}
              >
                <Card className={`h-full bg-card border-2 ${plan.color} ${plan.popular ? "relative scale-105 shadow-lg shadow-primary/10" : ""}`}>
                  {plan.popular && (
                    <div className="absolute -top-4 left-1/2 -translate-x-1/2">
                      <Badge className="bg-primary text-primary-foreground px-4 py-1">
                        Most Popular
                      </Badge>
                    </div>
                  )}
                  <CardHeader className="text-center pb-2 pt-8">
                    <CardTitle className="font-secondary text-2xl mb-2">{plan.name}</CardTitle>
                    <div className="mb-2">
                      <span className="font-secondary text-5xl font-bold">{plan.price}</span>
                      <span className="text-muted-foreground">{plan.period}</span>
                    </div>
                    <p className="text-muted-foreground">{plan.description}</p>
                  </CardHeader>
                  <CardContent className="pt-6">
                    <ul className="space-y-3 mb-8">
                      {plan.features.map((feature, j) => (
                        <li key={j} className="flex items-center gap-3">
                          {feature.included ? (
                            <Check className="w-5 h-5 text-primary shrink-0" />
                          ) : (
                            <X className="w-5 h-5 text-muted-foreground shrink-0" />
                          )}
                          <span className={feature.included ? "" : "text-muted-foreground"}>
                            {feature.text}
                          </span>
                        </li>
                      ))}
                    </ul>
                    <Link to={user ? "/dashboard" : "/register"}>
                      <Button 
                        className={`w-full ${plan.popular ? "glow-primary" : ""}`}
                        variant={plan.popular ? "default" : "outline"}
                        data-testid={`pricing-${plan.name.toLowerCase()}-btn`}
                      >
                        {plan.cta}
                        <ChevronRight className="w-4 h-4 ml-2" />
                      </Button>
                    </Link>
                  </CardContent>
                </Card>
              </motion.div>
            ))}
          </div>

          {/* B2B Section */}
          <Card className="mb-20 bg-card/50 border-border overflow-hidden">
            <div className="grid md:grid-cols-2 gap-8">
              <div className="p-8 md:p-12">
                <Badge className="mb-4 bg-purple-500/20 text-purple-400 border-purple-500/30">
                  Enterprise
                </Badge>
                <h2 className="font-secondary text-3xl font-bold mb-4">
                  For Teams & Companies
                </h2>
                <p className="text-muted-foreground mb-6">
                  Get custom solutions for your organization. Access our talent pool, 
                  run private hackathons, and train your team with tailored content.
                </p>
                <ul className="space-y-3 mb-8">
                  <li className="flex items-center gap-2">
                    <Users className="w-5 h-5 text-purple-400" />
                    <span>Access to top developer profiles</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <Trophy className="w-5 h-5 text-purple-400" />
                    <span>Hackathon-as-a-Service</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <Code2 className="w-5 h-5 text-purple-400" />
                    <span>Corporate training platform</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <Shield className="w-5 h-5 text-purple-400" />
                    <span>Custom security challenges</span>
                  </li>
                </ul>
                <Button className="glow-purple bg-purple-600 hover:bg-purple-700">
                  Contact Sales
                </Button>
              </div>
              <div 
                className="hidden md:block bg-cover bg-center"
                style={{
                  backgroundImage: `url(https://images.unsplash.com/photo-1639152201720-5e536d254d81?crop=entropy&cs=srgb&fm=jpg&q=85)`,
                  minHeight: "300px"
                }}
              />
            </div>
          </Card>

          {/* FAQ */}
          <div className="max-w-3xl mx-auto">
            <h2 className="font-secondary text-3xl font-bold text-center mb-8">
              Frequently Asked Questions
            </h2>
            <div className="space-y-4">
              {faqs.map((faq, i) => (
                <Card key={i} className="bg-card border-border">
                  <CardContent className="p-6">
                    <h3 className="font-semibold mb-2">{faq.q}</h3>
                    <p className="text-muted-foreground">{faq.a}</p>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </motion.div>
      </main>

      {/* Footer */}
      <footer className="border-t border-border py-12 px-4">
        <div className="max-w-7xl mx-auto">
          <div className="flex flex-col md:flex-row justify-between items-center gap-6">
            <div className="flex items-center gap-2">
              <Boxes className="w-6 h-6 text-primary" />
              <span className="font-secondary text-lg font-bold">CodeChain</span>
            </div>
            
            <div className="flex items-center gap-6 text-sm text-muted-foreground">
              <Link to="/problems" className="hover:text-foreground transition-colors">Problems</Link>
              <Link to="/leaderboard" className="hover:text-foreground transition-colors">Leaderboard</Link>
              <Link to="/hackathons" className="hover:text-foreground transition-colors">Hackathons</Link>
              <Link to="/pricing" className="hover:text-foreground transition-colors">Pricing</Link>
            </div>
            
            <div className="text-sm text-muted-foreground">
              © 2024 CodeChain. All rights reserved.
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Pricing;
