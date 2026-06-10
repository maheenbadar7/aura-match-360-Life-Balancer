import os

class AuraMatchApp:
    def __init__(self):
        print("--- Welcome to AuraMatch: Your 360° Life Balancer ---")
        self.name = input("Enter user name: ")
        self.age = input("Enter user age: ")
        self.personality = input("Enter personality type: ")
        self.interests = [i.strip().lower() for i in input("Enter interests (comma separated): ").split(",")]
        
        # Defining the IDEAL weekly benchmarks
        self.IDEAL_WORK = 40
        self.IDEAL_FAMILY = 25
        self.IDEAL_ME_TIME = 15
        self.IDEAL_GYM_WALK = 15
        self.IDEAL_SLEEP = 56

        # Starting baseline scores
        self.stress_level = 75 
        self.health_score = 60
        
        # Runtime variables to hold user inputs for visualizer & smart actions
        self.user_hours = {}

    def calculate_life_wheel(self):
        print(f"\n--- {self.name}'s Weekly Life Wheel Input ---")
        print("Please enter your hours for this week.")
        print("💡 Note the ideal hours shown in brackets to get the best Aura score!\n")
        
        # Adding ideal hours directly inside the input text prompts
        work = float(input(f"Enter Work / Study hours [Ideal: {self.IDEAL_WORK}h]: "))
        family = float(input(f"Enter Family & Friends hours [Ideal: {self.IDEAL_FAMILY}h]: "))
        me_time = float(input(f"Enter 'Me Time' hours [Ideal: {self.IDEAL_ME_TIME}h]: "))
        health_gym = float(input(f"Enter Gym & Walking hours [Ideal: {self.IDEAL_GYM_WALK}h]: "))
        sleep = float(input(f"Enter Sleep hours [Ideal: {self.IDEAL_SLEEP}h]: "))
        
        # Store for use in features 1 and 2
        self.user_hours = {
            "Work/Study": (work, self.IDEAL_WORK),
            "Family/Friends": (family, self.IDEAL_FAMILY),
            "Me Time": (me_time, self.IDEAL_ME_TIME),
            "Health/Gym": (health_gym, self.IDEAL_GYM_WALK),
            "Sleep": (sleep, self.IDEAL_SLEEP)
        }
        
        # Reset scores for a fresh calculation
        self.stress_level = 75
        self.health_score = 60

        print("\n--- Processing 360° Scenario Match... ---")
        
        # Math comparison against Ideals
        if sleep < self.IDEAL_SLEEP:
            print(f"⚠️ Sleep is below the ideal {self.IDEAL_SLEEP} hours.")
            self.stress_level += 15
            self.health_score -= 10
        else:
            print("✅ Great sleep routine matched!")
            self.stress_level -= 10
            self.health_score += 10

        if work > self.IDEAL_WORK + 5:
            print(f"⚠️ Overworking detected (Ideal is {self.IDEAL_WORK} hours).")
            self.stress_level += 20
            self.health_score -= 5
        else:
            print("✅ Work-life pacing is balanced!")
            self.stress_level -= 5

        if health_gym >= self.IDEAL_GYM_WALK:
            print("✅ Physical activity target achieved!")
            self.health_score += 15
            self.stress_level -= 10
        else:
            print(f"⚠️ Active time is less than the ideal {self.IDEAL_GYM_WALK} hours.")
            self.health_score -= 10

        # Boundary controls
        self.stress_level = max(10, min(100, self.stress_level))
        self.health_score = max(0, min(100, self.health_score))

    # --- FEATURE 1: AURA SCORE VISUALIZER (DASHBOARD) ---
    def show_aura_visualizer(self):
        print(f"\n==============================================")
        print(f"🔮  360° AURA BALANCE VISUALIZER DASHBOARD  🔮")
        print(f"==============================================")
        
        for sector, (actual, ideal) in self.user_hours.items():
            # Calculate match percentage (capped at 100% max for visual neatness)
            match_pct = min(100, int((actual / ideal) * 100)) if ideal > 0 else 0
            
            # Select color tone/emoji based on balancing accuracy
            if sector == "Work/Study" and actual > ideal + 5:
                status_emoji = "⚠️ [OVERLOADED]"
                bar_char = "❌"
            elif match_pct >= 85:
                status_emoji = "🟢 [PERFECTLY ALIGNED]"
                bar_char = "🟩"
            elif match_pct >= 50:
                status_emoji = "🟡 [MODERATE]"
                bar_char = "🟨"
            else:
                status_emoji = "🔴 [CRITICAL DROP]"
                bar_char = "🟥"
                
            # Render a visual tracking bar (1 block per 10%)
            bar_length = max(1, match_pct // 10)
            visual_bar = bar_char * bar_length + "⬜" * (10 - bar_length)
            
            print(f"{sector:<15} {visual_bar} {match_pct}% {status_emoji}")
        print(f"==============================================")

    # --- FEATURE 2: SMART MATCH RECOMMENDATIONS ---
    def trigger_smart_recommendations(self):
        print(f"\n🎯 Smart 'Match' Aura Actions:")
        has_recommendations = False
        
        work_actual, _ = self.user_hours["Work/Study"]
        family_actual, family_ideal = self.user_hours["Family/Friends"]
        me_actual, me_ideal = self.user_hours["Me Time"]
        
        # Rule A: Family Balance dropped below 50% of its target
        if (family_actual / family_ideal) < 0.50:
            print("💡 [Family Aura Boost]: Your Family Aura needs a shift! Schedule a 20-minute phone call or an evening walk with a family member today.")
            has_recommendations = True
            
        # Rule B: Overworked and low "Me Time"
        if work_actual > self.IDEAL_WORK and (me_actual / me_ideal) < 0.60:
            print("💡 [Mind & Soul Recharge]: Work hours are heavy while personal time is lagging. Set a hard stop on work tomorrow and take 30 minutes just for yourself to read or unplug.")
            has_recommendations = True
            
        if not has_recommendations:
            print("✨ Your Aura energy fields are beautifully distributed. No emergency correction moves needed right now!")

    # --- FEATURE 3: AURA TREND HISTORY (LOCAL LOGGER) ---
    def save_weekly_trend(self):
        filename = "aura_history.txt"
        overall_balance = (self.health_score + (100 - self.stress_level)) // 2
        
        try:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(f"User: {self.name} | Health: {self.health_score}/100 | Stress: {self.stress_level}% | Overall Balance: {overall_balance}%\n")
            print(f"\n💾 Weekly metrics successfully preserved in '{filename}'!")
        except Exception as e:
            print(f"\n⚠️ Unable to update trend file: {e}")

    def show_ultimate_reward(self):
        print(f"\n--- 📊 AuraMatch Ultimate Reward System ---")
        print(f"User: {self.name}")
        print(f"Current Stress Level: {self.stress_level}%")
        print(f"Overall Health Score: {self.health_score}/100")
        
        # Informing them how to reach the benchmark targets
        if self.stress_level <= 35 and self.health_score >= 90:
            print("\n🌟 PERFECT MATCH! Your hours perfectly mirror the Ideal Aura Blueprint.")
        else:
            print(f"\n💡 Hint: Align your hours closer to the ideal targets (Work: {self.IDEAL_WORK}h, Sleep: {self.IDEAL_SLEEP}h, etc.) to optimize your score!")

# --- CLEAN EXECUTION BLOCK ---
if __name__ == "__main__":
    app = AuraMatchApp()
    app.calculate_life_wheel()
    app.show_aura_visualizer()          # Feature 1 Dashboard
    app.trigger_smart_recommendations() # Feature 2 Actions
    app.save_weekly_trend()             # Feature 3 Data Storage
    app.show_ultimate_reward()
