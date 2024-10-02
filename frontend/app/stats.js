
'use client'
import { LineChart } from '@mui/x-charts/LineChart';
export default function Stats() {
    return (
        <div className=" p-5 bg-white min-w-[500px] rounded-lg shadow-md transition-transform transition-shadow hover:shadow-custom hover:translate-y-[-4.30px]">
            Stats
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