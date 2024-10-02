import { ChevronLeft } from "lucide-react";
export default function News() {
  return (
    <div className="p-5 bg-white min-w-[200px] rounded-lg shadow-md transition-transform transition-shadow hover:shadow-custom hover:translate-y-[-4.30px]">
      <div className="flex justify-between">Today News 

        <div>
          <ChevronLeft />
        </div>
      </div>
    </div>
  );
}