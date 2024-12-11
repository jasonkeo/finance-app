'use client'
import Image from "next/image";

import { useEffect, useState } from "react";
import News from "./news";
import Stats from "./stats";
import Analysis from "./analysis";
import api from "./api"
export default function Home() {

  const [data, setData] = useState(
    {
      "news": [],
      "index": {},
      "analysis": ""
    }
  );
  useEffect(() => {
    async function fetchData() {
      try {
        const fetchedData = await api();
        setData(fetchedData);
      } catch (error) {
        console.error("Error in fetchData function:", error);
      }
    }
    fetchData();
  }, []);

  return (
    <div className="flex items-center justify-center mt-10 background: #f3f4f6;">
      <div className="grid grid-rows-2 gap-5 p-5">
        
      <div className="flex flex-col lg:flex-row gap-5 flex-grow-0">
      <Stats stats={data['index']}/>

      <News news={data['news']}/>
    
      
    
    </div>
   
       

        <div className="flex-grow-0">
        <Analysis chat={data['analysis']}></Analysis>
        </div>
      </div>
    </div>
  );
}