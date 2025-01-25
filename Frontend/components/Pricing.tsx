import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Check } from "lucide-react"

const plans = [
  {
    name: "Basic",
    price: "$29.99",
    description: "Essential tools for individual investors",
    features: ["AI Portfolio Analysis", "Basic Market Predictions", "Daily Financial News Digest", "Email Support"],
  },
  {
    name: "Pro",
    price: "$99.99",
    description: "Advanced features for serious traders",
    features: [
      "All Basic features",
      "Real-time Market Alerts",
      "Advanced Predictive Analytics",
      "Customizable Dashboard",
      "Priority Support",
    ],
  },
  {
    name: "Enterprise",
    price: "Custom",
    description: "Tailored solutions for large institutions",
    features: [
      "All Pro features",
      "Dedicated Account Manager",
      "Custom API Integration",
      "On-premise Deployment Option",
      "24/7 Phone Support",
    ],
  },
]

export default function Pricing() {
  return (
    <section id="pricing" className="container py-24 sm:py-32">
      <h2 className="text-3xl font-bold tracking-tighter md:text-4xl mb-12 text-center">
        Choose the Right Plan for Your Financial Goals
      </h2>
      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {plans.map((plan, index) => (
          <Card key={index} className="flex flex-col justify-between">
            <CardHeader>
              <CardTitle>{plan.name}</CardTitle>
              <CardDescription>{plan.description}</CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-4xl font-bold mb-4">{plan.price}</p>
              <ul className="space-y-2">
                {plan.features.map((feature, featureIndex) => (
                  <li key={featureIndex} className="flex items-center">
                    <Check className="h-5 w-5 mr-2 text-green-500" />
                    {feature}
                  </li>
                ))}
              </ul>
            </CardContent>
            <CardFooter>
              <Button className="w-full">Get Started</Button>
            </CardFooter>
          </Card>
        ))}
      </div>
    </section>
  )
}

