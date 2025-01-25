import "@/styles/globals.css"
import { Inter } from "next/font/google"

const inter = Inter({ subsets: ["latin"] })

export const metadata = {
  title: "FinanceAI - AI-Powered Financial Insights",
  description:
    "FinanceAI provides AI-driven portfolio insights, comprehensive financial dashboards, and market movement predictions for smarter investing.",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  )
}



import './globals.css'