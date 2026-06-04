import { useEffect, useState } from "react";
import API from "../services/api";
import CostChart from "../components/CostChart";

function Dashboard() {
  const [report, setReport] = useState(null);

  useEffect(() => {
    API.get("/report")
      .then((res) => setReport(res.data))
      .catch((err) => console.log(err));
  }, []);

  if (!report)
    return (
      <div className="p-10 text-xl">
        Loading...
      </div>
    );

  return (
    <div className="min-h-screen bg-slate-100 p-8">
      <h1 className="text-4xl font-bold mb-8">
        AWS Cost Optimization Dashboard
      </h1>

      <div className="grid grid-cols-5 gap-6 mb-8">
        <div className="bg-white rounded-xl shadow p-6">
          <h3 className="text-gray-500">Monthly Cost</h3>
          <p className="text-3xl font-bold">$0.00</p>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <h3 className="text-gray-500">EC2 Instances</h3>
          <p className="text-3xl font-bold">
            {report.total_ec2_instances}
          </p>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <h3 className="text-gray-500">S3 Buckets</h3>
          <p className="text-3xl font-bold">
            {report.total_s3_buckets}
          </p>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <h3 className="text-gray-500">Recommendations</h3>
          <p className="text-3xl font-bold">
            {report.total_recommendations}
          </p>
        </div>
      </div>

      <div className="bg-green-100 rounded-xl shadow p-6">
  <h3 className="text-gray-700">
    Potential Savings
  </h3>

  <p className="text-3xl font-bold text-green-600">
    ${report.potential_monthly_savings}
  </p>
</div>

      <div className="bg-white rounded-xl shadow p-6">
        <h2 className="text-2xl font-bold mb-4">
          Optimization Recommendations
        </h2>

    <div className="mt-8">
  <CostChart report={report} />
</div>

        {report.recommendations.map((item, index) => (
          <div
            key={index}
            className="border rounded-lg p-4 mb-4"
          >
            <p className="font-semibold">
              {item.recommendation}
            </p>

            <p>{item.action}</p>

            <p className="text-green-600 font-bold">
              Savings: {item.estimated_savings}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Dashboard;