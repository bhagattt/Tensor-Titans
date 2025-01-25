import { Button } from "@/components/ui/button"

export default function CTA() {
  return (
    <section className="bg-muted py-24 sm:py-32">
      <div className="container flex flex-col items-center text-center">
        <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">
          Ready to Take Control of Your Financial Future?
        </h2>
        <p className="mt-4 text-lg text-muted-foreground max-w-[700px]">
          Join thousands of learners who are improving their financial literacy and making smarter investment decisions
          with FinanceAI.
        </p>
        <Button size="lg" className="mt-8">
          Start Your Free Learning Journey
        </Button>
      </div>
    </section>
  )
}

