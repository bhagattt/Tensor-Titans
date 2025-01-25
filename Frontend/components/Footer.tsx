import Link from "next/link"
import { Facebook, Twitter, Instagram, Linkedin } from "lucide-react"

export default function Footer() {
  return (
    <footer className="border-t bg-background">
      <div className="container flex flex-col gap-8 py-8 md:flex-row md:py-12">
        <div className="flex-1">
          <Link href="/" className="flex items-center space-x-2">
            <span className="inline-block font-bold">FinanceAI</span>
          </Link>
        </div>
        <div className="grid flex-1 grid-cols-2 gap-8 sm:grid-cols-3">
          <div className="flex flex-col gap-2">
            <h3 className="font-semibold">Product</h3>
            <Link href="#features" className="text-sm text-muted-foreground">
              AI Portfolio Insights
            </Link>
            <Link href="#features" className="text-sm text-muted-foreground">
              Dashboard
            </Link>
            <Link href="#features" className="text-sm text-muted-foreground">
              Predict Movements
            </Link>
          </div>
          <div className="flex flex-col gap-2">
            <h3 className="font-semibold">Company</h3>
            <Link href="#" className="text-sm text-muted-foreground">
              About
            </Link>
            <Link href="#" className="text-sm text-muted-foreground">
              Careers
            </Link>
            <Link href="#" className="text-sm text-muted-foreground">
              Contact
            </Link>
          </div>
          <div className="flex flex-col gap-2">
            <h3 className="font-semibold">Legal</h3>
            <Link href="#" className="text-sm text-muted-foreground">
              Privacy Policy
            </Link>
            <Link href="#" className="text-sm text-muted-foreground">
              Terms of Service
            </Link>
            <Link href="#" className="text-sm text-muted-foreground">
              Security
            </Link>
          </div>
        </div>
      </div>
      <div className="container flex flex-col gap-4 py-4 md:flex-row md:items-center md:justify-between md:py-6">
        <p className="text-sm text-muted-foreground">© 2023 FinanceAI. All rights reserved.</p>
        <div className="flex gap-4">
          <Link href="#" className="text-muted-foreground hover:text-foreground">
            <Facebook className="h-5 w-5" />
            <span className="sr-only">Facebook</span>
          </Link>
          <Link href="#" className="text-muted-foreground hover:text-foreground">
            <Twitter className="h-5 w-5" />
            <span className="sr-only">Twitter</span>
          </Link>
          <Link href="#" className="text-muted-foreground hover:text-foreground">
            <Instagram className="h-5 w-5" />
            <span className="sr-only">Instagram</span>
          </Link>
          <Link href="#" className="text-muted-foreground hover:text-foreground">
            <Linkedin className="h-5 w-5" />
            <span className="sr-only">LinkedIn</span>
          </Link>
        </div>
      </div>
    </footer>
  )
}

