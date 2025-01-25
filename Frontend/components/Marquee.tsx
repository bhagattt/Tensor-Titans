"use client"

import { useEffect, useState } from "react"
import { ArrowUpRight, ArrowDownRight } from "lucide-react"

const stockData = [
  { symbol: "RELIANCE", price: 2500.75, change: 1.5 },
  { symbol: "TCS", price: 3450.2, change: -0.8 },
  { symbol: "HDFCBANK", price: 1650.3, change: 0.6 },
  { symbol: "INFY", price: 1320.45, change: -1.2 },
  { symbol: "ICICIBANK", price: 950.8, change: 2.1 },
]

export default function Marquee() {
  const [stocks, setStocks] = useState(stockData)

  useEffect(() => {
    const interval = setInterval(() => {
      setStocks((prevStocks) =>
        prevStocks.map((stock) => ({
          ...stock,
          price: +(stock.price + (Math.random() - 0.5) * 10).toFixed(2),
          change: +((Math.random() - 0.5) * 4).toFixed(2),
        })),
      )
    }, 5000)

    return () => clearInterval(interval)
  }, [])

  return (
    <div className="bg-muted py-2 overflow-hidden">
      <div className="flex animate-marquee whitespace-nowrap">
        {stocks.concat(stocks).map((stock, index) => (
          <div key={index} className="mx-4 flex items-center">
            <span className="font-bold">{stock.symbol}</span>
            <span className="ml-2">₹{stock.price.toFixed(2)}</span>
            <span className={`ml-2 flex items-center ${stock.change >= 0 ? "text-green-500" : "text-red-500"}`}>
              {stock.change >= 0 ? <ArrowUpRight size={16} /> : <ArrowDownRight size={16} />}
              {Math.abs(stock.change).toFixed(2)}%
            </span>
          </div>
        ))}
      </div>
    </div>
  )
}

