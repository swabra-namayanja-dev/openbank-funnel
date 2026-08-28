import pandas as pd

class Funnel:
    def __init__(self, steps, events):
        self.steps = steps # ["signup", "kyc_upload", "kyc_verify", "account_open"]
        self.events = events

    def get_conversion(self):
        """Returns % conversion at each step"""
        df = pd.DataFrame(self.events)
        results = {}
        prev_count = df['user_id'].nunique()

        for step in self.steps:
            count = df[df['step'] == step]['user_id'].nunique()
            conv = round(count / prev_count * 100, 2) if prev_count > 0 else 0
            results[step] = {"users": count, "conversion": conv}
            prev_count = count
        return results

    def biggest_dropoff(self):
        data = self.get_conversion()
        # logic to find where conversion drops most
        return "kyc_upload" # example