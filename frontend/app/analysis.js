import chatgpt from "./chatgpt"
import { useState, useEffect} from "react";

export default function Analysis() {
  var [chat, changeChat] = useState("");  
  useEffect(() => {
    async function fetchData() {
      const model = await chatgpt();
      changeChat(model);
      console.log(model);
    }
    fetchData();
    }, []);

    return (
      <div className="p-5 bg-white w-full rounded-lg shadow-md transition-transform transition-shadow hover:shadow-custom hover:translate-y-[-4.30px]">
        <strong>Analysis</strong>
        <p>{chat}</p>
      </div>
    );
  }