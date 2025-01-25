import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { LineChart, BookOpen, TrendingUp } from "lucide-react"

const features = [
  {
    icon: LineChart,
    title: "AI Portfolio Insights",
    description:
      "Learn how AI analyzes your portfolio and get personalized educational content to understand investment strategies.",
  },
  {
    icon: BookOpen,
    title: "Financial Education Hub",
    description:
      "Access a comprehensive library of financial topics, from basics to advanced concepts, tailored to your learning pace.",
  },
  {
    icon: TrendingUp,
    title: "Market Trends Explained",
    description:
      "Understand market movements with AI-driven explanations, helping you make informed decisions based on data.",
  },
]

export default function Features() {
  return (
    <section id="features" className="container py-24 sm:py-32">
      <h2 className="text-3xl font-bold tracking-tighter md:text-4xl mb-12 text-center">Smart Asset Allocation</h2>
      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {features.map((feature, index) => (
          <Card key={index}>
            <CardHeader>
              <feature.icon className="h-10 w-10 mb-2" />
              <CardTitle>{feature.title}</CardTitle>
            </CardHeader>
            <CardContent>
              <CardDescription>{feature.description}</CardDescription>
            </CardContent>
          </Card>
        ))}
      </div>
    </section>
  )
}

