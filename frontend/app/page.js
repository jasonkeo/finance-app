'use client'
import Image from "next/image";
import Get from "./infomation";
import { useEffect, useState } from "react";
export default function Home() {
  const [news, setNews] = useState([]);
  
  useEffect(() => {
    async function fetchData() {
      const data = await Get();
      setNews(data); 
    }
    
    fetchData();
  }, []); 

  return (
    <div className="border-2 border-black max-w-[200px]">
      {news.map((item) => (
        <div key={item.id}>
          <div>Date: {item.date}</div>
          <div>News:</div>
          <ul>
            {item.news.map((newsItem, index) => (
              <li key={index}>{newsItem}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}