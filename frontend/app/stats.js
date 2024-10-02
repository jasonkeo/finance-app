
'use client'
import { LineChart } from '@mui/x-charts/LineChart';
export default function Stats() {
    return (
        <div className=" p-5 bg-white min-w-[500px] rounded-lg shadow-md transition-transform transition-shadow hover:shadow-custom hover:translate-y-[-4.30px]">
            <div className='flex justify-between'> Stats 
            <select className="ml-2 p-1 border rounded">
                    <option value="option1">Option 1</option>
                    <option value="option2">Option 2</option>
                    <option value="option3">Option 3</option>
                </select>
            </div>
            <LineChart
                xAxis={[{ data: [1, 2, 3, 5, 8, 10] }]}
                series={[
                    {
                        data: [2, 5.5, 2, 8.5, 1.5, 5],
                    },
                ]}
                width={500}
                height={300}
            />
        </div>
    );
}