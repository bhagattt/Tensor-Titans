import Image from "next/image"

const testimonials = [
  {
    quote: "FinanceAI's predictive analytics have significantly improved our investment strategy.",
    author: "Sarah Johnson",
    role: "Portfolio Manager, Capital Investments",
  },
  {
    quote: "The AI-driven insights have helped us identify market trends before they become mainstream.",
    author: "Michael Chen",
    role: "Chief Investment Officer, Tech Ventures Fund",
  },
  {
    quote: "FinanceAI's dashboard has streamlined our financial decision-making process tremendously.",
    author: "Emma Rodriguez",
    role: "Financial Analyst, Global Assets Management",
  },
]

export default function Testimonials() {
  return (
    <section id="testimonials" className="container py-24 sm:py-32">
      <h2 className="text-3xl font-bold tracking-tighter md:text-4xl mb-12 text-center">
        Trusted by Financial Professionals
      </h2>
      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {testimonials.map((testimonial, index) => (
          <blockquote key={index} className="rounded-lg bg-muted p-6 shadow">
            <p className="mb-4 text-lg">{testimonial.quote}</p>
            <footer className="flex items-center space-x-4">
              <Image
                src={`https://i.pravatar.cc/60?img=${index + 1}`}
                alt={testimonial.author}
                className="rounded-full"
                width={40}
                height={40}
              />
              <div>
                <p className="text-sm font-semibold">{testimonial.author}</p>
                <p className="text-sm text-muted-foreground">{testimonial.role}</p>
              </div>
            </footer>
          </blockquote>
        ))}
      </div>
    </section>
  )
}

