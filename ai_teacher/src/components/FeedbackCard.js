export default function FeedbackCard({ feedback }) {
    return (
      <div className="p-4 border rounded bg-white shadow-md mt-4">
        <h3 className="text-md font-semibold">Feedback</h3>
        <p className="mt-2 text-gray-700">{feedback}</p>
      </div>
    );
  }