import { Button } from "@/components/ui/button"
import Image from "next/image"

export default function Hero() {
  return (
    <section className="container flex flex-col gap-4 pb-8 pt-6 md:pb-12 md:pt-10 lg:py-32">
      <div className="flex flex-col lg:flex-row items-center gap-8">
        <div className="flex-1 flex flex-col items-start gap-4">
          <h1 className="text-3xl font-extrabold leading-tight tracking-tighter md:text-4xl">
            Empowering Financial Literacy
            <br className="hidden sm:inline" />
            for Everyone
          </h1>
          <p className="max-w-[700px] text-lg text-muted-foreground">
            FinanceAI combines cutting-edge artificial intelligence with comprehensive financial education to help you
            make informed decisions. Learn, grow, and invest smarter with us.
          </p>
          <div className="flex gap-4">
            <Button size="lg">Start Learning</Button>
            <Button size="lg" variant="outline">
              Explore Features
            </Button>
          </div>
        </div>
        <div className="flex-1 mt-8 lg:mt-0">
          <Image
            src="/finance-education.jpg"
            width={600}
            height={400}
            alt="Financial education illustration"
            className="rounded-md object-cover"
          />
        </div>
      </div>
    </section>
  )
}

