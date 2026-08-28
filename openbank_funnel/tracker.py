import datetime

class FunnelTracker:
    def __init__(self):
        self.events = [] # in real app, this is PostgreSQL

    def track_step(self, user_id, step_name):
        """Track when user hits a step: signup, kyc_upload, kyc_verify, account_open"""
        self.events.append({
            "user_id": user_id,
            "step": step_name,
            "timestamp": datetime.datetime.now()
        })
        print(f"Tracked: User {user_id} at {step_name}")

tracker = FunnelTracker()