import { ChevronLeft, ChevronRight } from "lucide-react";
import infomation from "./infomation";
import { useEffect, useState } from "react";
export default function News() {
  const [news, changenews] = useState(null);
  const [index, changeindex] = useState(0);

  useEffect(() => {
    async function fetchData() {
      const data = await infomation();
      changenews(data);
      console.log(data); 
    }
    fetchData();
    
  },[]);

  function indexupdate(num) {
    let temp = index;
    if (num > 0) {
      temp++
      if (index > news.length - 1) {
        temp = 0;
      }
    }
    else {
      
      if (index < 1 ) {
        temp = news.length - 1;

      } else {
        temp--
      }

    }
    if (index == null) {
      return;
    }
    
   
    changeindex(temp)
    
  }

  return (
    <div className="p-5 bg-white lg:max-w-[300px] rounded-lg shadow-md transition-transform transition-shadow hover:shadow-custom hover:translate-y-[-4.30px]">
      <div className="flex justify-between"><strong>Today News</strong> 
      
        <div className="flex no-wrap whitespace-nowrap">
          <button onClick={() =>indexupdate(-1)}><ChevronLeft /></button>
          <button onClick={() => indexupdate(1)}><ChevronRight /></button>
        </div>

      </div>

      <div className="mt-2 flex-wrap over-flow-scroll">{news? (news.map(( (item) => ( <li>{item[index]}</li>) )) ) : (<p> loading... </p> ) }</div>
    </div>
  );
}