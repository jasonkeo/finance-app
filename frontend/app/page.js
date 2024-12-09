'use client'
import Image from "next/image";
import Get from "./infomation";
import { useEffect, useState } from "react";
import News from "./news";
import Stats from "./stats";
import Analysis from "./analysis";
export default function Home() {


  return (
    <div className="flex items-center justify-center mt-10 background: #f3f4f6;">
      <div className="grid grid-rows-2 gap-5 p-5">
        
      <div className="flex flex-col lg:flex-row gap-5">
      <Stats />

      <News/>
    
      
    
    </div>
   
       

        <div className="">
        <Analysis></Analysis>
        </div>
      </div>
    </div>
  );
}