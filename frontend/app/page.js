'use client'
import Image from "next/image";
import Get from "./infomation";
import { useEffect, useState } from "react";
import News from "./news";
import Stats from "./stats";
import Analysis from "./analysis";
export default function Home() {


  return (
    <div className="flex items-center justify-center mt-10  background: #f3f4f6;">
      <div className="grid grid-cols-3 grid-rows-2 gap-5">
        
      <div className="col-span-1">
      <News />
    </div>
    <div className="col-span-2">
      <Stats />
    </div>
       

        <div className="col-span-3">
        <Analysis></Analysis>
        </div>
      </div>
    </div>
  );
}