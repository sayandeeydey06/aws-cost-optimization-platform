import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

function CostChart({ report }) {
  const data = [
    {
      name: "EC2",
      value: report.total_ec2_instances,
    },
    {
      name: "S3",
      value: report.total_s3_buckets,
    },
    {
      name: "Recommendations",
      value: report.total_recommendations,
    },
  ];

  return (
    <div className="bg-white rounded-xl shadow p-6">
      <h2 className="text-2xl font-bold mb-4">
        Resource Overview
      </h2>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
         <Bar
  dataKey="value"
  fill="#3B82F6"
  radius={[8, 8, 0, 0]}
/>
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default CostChart;