
import ReactMarkdown from 'react-markdown';
export default function Analysis({chat}) {
   
 

    return (
      <div className="p-5 bg-white max-w-[820px] max-h-[370px] overflow-y-scroll rounded-lg shadow-md transition-transform transition-shadow hover:shadow-custom hover:translate-y-[-4.30px]">
        <u><strong>Analysis Done By Chatgpt</strong></u>
        <ReactMarkdown> 
          {chat}
</ReactMarkdown>
      </div>
    );
  }