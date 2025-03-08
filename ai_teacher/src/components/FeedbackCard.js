export default function FeedbackCard({ feedback }) {
    return (
      <div className="feedback-card">
        <h3>Feedback</h3>
        <p>{feedback}</p>
      </div>
    );
  }