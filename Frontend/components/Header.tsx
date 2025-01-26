import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function Header() {
  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-32 items-center justify-center space-x-4 sm:justify-between sm:space-x-0">
        <div className="flex gap-6 md:gap-10">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-2">
            <span className="inline-block text-3xl font-bold">Stock Sure</span>
          </Link>

          {/* Navigation Links */}
          <nav className="hidden md:flex gap-6">
            <Link
              href="/recommend"
              className="flex items-center text-base font-medium text-muted-foreground hover:text-primary py-2"
            >
              AI Portfolio Insights
            </Link>
            <Link
              href="/asset" // Add this link for AI Asset Allocation
              className="flex items-center text-base font-medium text-muted-foreground hover:text-primary py-2"
            >
              AI Asset Allocation
            </Link>
            <Link
              href="#features"
              className="flex items-center text-base font-medium text-muted-foreground hover:text-primary py-2"
            >
              Dashboard
            </Link>
            <Link
              href="/predict"
              className="flex items-center text-base font-medium text-muted-foreground hover:text-primary py-2"
            >
              Predict Movements
            </Link>
            <Link
              href="/market-trend"
              className="flex items-center text-base font-medium text-muted-foreground hover:text-primary py-2"
            >
              Market Trend
            </Link>
          </nav>
        </div>

        {/* Login/Signup Buttons */}
        <div className="flex flex-1 items-center justify-end space-x-4">
          <nav className="flex items-center space-x-2">
            <Button variant="ghost" size="default">
              Log in
            </Button>
            <Button size="default">Sign up</Button>
          </nav>
        </div>
      </div>
    </header>
  );
}