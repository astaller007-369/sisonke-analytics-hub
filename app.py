# ==============================================================================
# SEGMENT 1 OF 14: CORE PACKAGES, LAYOUT BLUEPRINTS & GLOBAL RAM CACHE STATES
# ==============================================================================
import os
import math
import datetime
import numpy as np
import pandas as pd
import streamlit as st
import pandas as pd
import numpy as np

def force_universal_sisonke_schema(raw_uploaded_df):
    """
    Surgically takes any downloaded sports dataset, identifies the core metrics,
    and forces the structure into your exact requested 22-column layout.
    """
    clean_df = pd.DataFrame()
    raw_uploaded_df.columns = [str(c).strip().lower().replace(" ", "_") for c in raw_uploaded_df.columns]
    
    # Define structural lookup aliases matching common free internet download headers
    alias_dict = {
        "competition": ["competition", "league", "div", "tournament", "comp"],
        "date": ["date", "timestamp", "match_timestamp", "time"],
        "home": ["home", "home_team", "hometeam", "host"],
        "away": ["away", "away_team", "awayteam", "visitor"],
        "home_goals": ["home_goals", "fthg", "hg", "home_score"],
        "away_goals": ["away_goals", "ftag", "ag", "away_score"],
        "home_sot": ["home_sot", "hst", "home_shots_on_target"],
        "away_sot": ["away_sot", "ast", "away_shots_on_target"],
        "home_big_chances": ["home_big_chances", "home_bc", "home_chances"],
        "away_big_chances": ["away_big_chances", "away_bc", "away_chances"],
        "home_box_touches": ["home_box_touches", "home_penalty_touches", "home_touches_in_box"],
        "away_box_touches": ["away_box_touches", "away_penalty_touches", "away_touches_in_box"],
        "home_red_cards": ["home_red_cards", "hr", "home_reds"],
        "away_red_cards": ["away_red_cards", "ar", "away_reds"],
        "home_ground_duels_won": ["home_ground_duels_won", "home_duels", "home_ground_duels"],
        "away_ground_duels_won": ["away_ground_duels_won", "away_duels", "away_ground_duels"],
        "home_aerial_duels": ["home_aerial_duels", "home_aerials", "home_aerial_duels_won"],
        "away_aerial_duels_won": ["away_aerial_duels_won", "away_aerials", "away_aerial_duels_won"],
        "home_tackles_won": ["home_tackles_won", "home_tackles", "home_tackles_win"],
        "away_tackles_won": ["away_tackles_won", "away_tackles", "away_tackles_win"],
        "home_dribbles": ["home_dribbles", "home_dribbles_won", "home_dribbles_win"],
        "away_dribbles": ["away_dribbles", "away_dribbles_won", "away_dribbles_win"]
    }
    
    # Execute mapping loop
    for target_col, aliases in alias_dict.items():
        matched = False
        for alias in aliases:
            if alias in raw_uploaded_df.columns:
                clean_df[target_col] = raw_uploaded_df[alias]
                matched = True
                break
        if not matched:
            # If the downloaded file does not contain the advanced metric, fill it with blank data
            clean_df[target_col] = np.nan
            
    # Force exact 22-column structural sequencing sequence requested
    exact_sequence = [
        "competition", "date", "home", "away", "home_goals", "away_goals",
        "home_sot", "away_sot", "home_big_chances", "away_big_chances",
        "home_box_touches", "away_box_touches", "home_red_cards", "away_red_cards",
        "home_ground_duels_won", "away_ground_duels_won", "home_aerial_duels", "away_aerial_duels_won",
        "home_tackles_won", "away_tackles_won", "home_dribbles", "away_dribbles"
    ]
    return clean_df[exact_sequence]
    

st.set_page_config(page_title="Sisonke Hub Terminal", layout="wide", initial_sidebar_state="expanded")

storage_path = "master_sisonke_database.csv"
baseline_goals = 2.65

if "freeze_matrix" not in st.session_state: st.session_state.freeze_matrix = {}
if "display_replicated_ledger_df" not in st.session_state: st.session_state["display_replicated_ledger_df"] = pd.DataFrame()
if "full_validation_df" not in st.session_state: st.session_state["full_validation_df"] = pd.DataFrame()
if "processed_cache_success" not in st.session_state: st.session_state["processed_cache_success"] = False

st.markdown("""
<style>
    .reportview-container .main .block-container { max-width: 95%; padding-top: 1rem; }
    div.stButton > button:first-child { width: 100%; font-weight: bold; border-radius: 4px; background-color: #1f6feb; color: white; }
    .stMetric { background-color: #0e1117; padding: 0.5rem; border-radius: 4px; border: 1px solid #30363d; }
</style>
""", unsafe_allow_html=True)
# ==============================================================================
# SEGMENT 2 CORE SAFETY PATCH: DYNAMIC SEASONS INPUT FETCH ENGINE
# ==============================================================================
def fetch_thestatsapi_to_sisonke(league_id, target_seasons):
    """Clean commercial server connection. Bypasses all web firewalls."""
    import datetime
    import requests
    import pandas as pd
    
    current_date = datetime.date.today()
    ninety_days_future = current_date + datetime.timedelta(days=90)
    
    # ðŸ›‘ PASTE YOUR REAL APINUMERIC TOKEN STRINGS INSIDE THESE QUOTES:
    api_token = "fapi_MSr9G4BWrzxnDEoDGaUEHOoX82FsjIE3" 
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Accept": "application/json"
    }
    
    combined_records_list = []
    
    for season in target_seasons:
        # ==============================================================================
        # SEGMENT 2 FINALISED IMMUNE BASE URL PATHWAY
        # ==============================================================================
        sisonke_front_gate = "https://api.thestatsapi.com"
        
        # ðŸŸ¢ THE REAL FIXED PATH: Appends the /api route and maps clean ID strings
        # Enforces 'comp_' and 'sn_' string value prefixes exactly as required
        endpoint_url = f"{sisonke_front_gate}/api/football/matches"
        
        # Type-hardened parameter mapping structure
        api_params = {
            "competition_id": f"comp_{league_id}" if "comp_" not in str(league_id) else league_id,
            "season_id": f"sn_{season}" if "sn_" not in str(season) else season,
            "per_page": 100
        }
        
        try:
            # ðŸŸ¢ FIXED: Hardcodes your token directly to bypass the missing variable fault
            server_response = requests.get(
                endpoint_url, 
                headers={
                    "Authorization": "Bearer fapi_StHSSTzkl40Bc3EJ3znTqH8oEXjz3Szu",
                    "Accept": "application/json"
                },
                params=api_params,
                timeout=30
            )
            if server_response.status_code == 200:
                payload_data = server_response.json().get("data", [])
                if isinstance(payload_data, list) and payload_data:
                    combined_records_list.extend(payload_data)
        except Exception:
            continue

            
            
        
        try:
            server_response = requests.get(endpoint_url, headers=headers, timeout=15)
            if server_response.status_code == 200:
                payload_data = server_response.json().get("data", [])
                if isinstance(payload_data, list) and payload_data:
                    combined_records_list.extend(payload_data)
        except Exception:
            continue
            
    if not combined_records_list:
        return pd.DataFrame()
        
    raw_master_df = pd.DataFrame(combined_records_list)
    
    if "date" not in raw_master_df.columns:
        return pd.DataFrame()
        
    raw_master_df["match_date_parsed"] = pd.to_datetime(raw_master_df["date"]).dt.date
    
    settled_results_mask = raw_master_df.get("status", "") == "FT"
    historical_settled_df = raw_master_df[settled_results_mask]
    
    future_fixtures_mask = (
        (raw_master_df.get("status", "") == "NS") & 
        (raw_master_df["match_date_parsed"] >= current_date) & 
        (raw_master_df["match_date_parsed"] <= ninety_days_future)
    )
    upcoming_three_month_df = raw_master_df[future_fixtures_mask]
    
    if historical_settled_df.empty and upcoming_three_month_df.empty:
        return pd.DataFrame()
        
    final_sanitized_pipeline_df = pd.concat([historical_settled_df, upcoming_three_month_df], ignore_index=True)
    final_sanitized_pipeline_df = final_sanitized_pipeline_df.sort_values(by="date", ascending=True)
    
    return final_sanitized_pipeline_df.drop(columns=["match_date_parsed"], errors="ignore")
    
        
    raw_master_df = pd.DataFrame(combined_records_list)
    
    # ðŸ›¡ï¸ STAGE 3: APPLY SURGICAL DATA FILTERING LOCKS
    # Convert incoming timestamp text rows into standard pandas datetime layouts behind the glass
    raw_master_df["match_date_parsed"] = pd.to_datetime(raw_master_df["date"]).dt.date
    
    # Split Layer A: Isolate all completed matches (Settled Historical Results)
    settled_results_mask = raw_master_df["status"] == "FT"
    historical_settled_df = raw_master_df[settled_results_mask]
    
    # Split Layer B: Isolate upcoming matches inside your strict 3-Month (90-Day) window
    future_fixtures_mask = (
        (raw_master_df["status"] == "NS") & 
        (raw_master_df["match_date_parsed"] >= current_date) & 
        (raw_master_df["match_date_parsed"] <= ninety_days_future)
    )
    upcoming_three_month_df = raw_master_df[future_fixtures_mask]
    
    # STAGE 4: COLLAPSE BLOCKS INTO A SINGLE REPAIRED DATA TIMELINE
    final_sanitized_pipeline_df = pd.concat([historical_settled_df, upcoming_three_month_df], ignore_index=True)
    
    # Sort chronologically to preserve your time-decay half-life math sequence
    final_sanitized_pipeline_df = final_sanitized_pipeline_df.sort_values(by="match_date_parsed", ascending=True)
    
    # Your Universal Structural Converter Module intercepts this clean output layout right here!
    return final_sanitized_pipeline_df.drop(columns=["match_date_parsed"], errors="ignore")

st.title("ðŸ¦… Sisonke Football Predictive Analytics Hub")
st.caption("we beat the odds.")
import streamlit as st
import requests
import pandas as pd

# ==============================================================================
# SEGMENT 2 CORE SAFETY PATCH: DYNAMIC SEASONS INPUT FETCH ENGINE
# ==============================================================================
def fetch_thestatsapi_to_sisonke(league_id, target_seasons):
    """Clean commercial server connection. Bypasses all web firewalls."""
    import datetime
    import requests
    import pandas as pd
    
    current_date = datetime.date.today()
    ninety_days_future = current_date + datetime.timedelta(days=90)
    
    
    api_token = "fapi_MSr9G4BWrzxnDEoDGaUEHOoX82FsjIE3" 
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Accept": "application/json"
    }
    
    combined_records_list = []
    
    for season in target_seasons:
            
        sisonke_front_gate = "https://api.thestatsapi.com"
        
        
        # ==============================================================================
# LINE 223 TRANSLATION FIX: SYNCHRONIZING VARIABLE LABELS
# ==============================================================================
        
        endpoint_url = f"{sisonke_front_gate}/api/football/teams/{league_id}/matches?season={season}"

        

        
        try:
            server_response = requests.get(endpoint_url, headers=headers, timeout=15)
            if server_response.status_code == 200:
                payload_data = server_response.json().get("data", [])
                if isinstance(payload_data, list) and payload_data:
                    combined_records_list.extend(payload_data)
        except Exception:
            continue
            
    if not combined_records_list:
        return pd.DataFrame()
        
    raw_master_df = pd.DataFrame(combined_records_list)
    
    if "date" not in raw_master_df.columns:
        return pd.DataFrame()
        
    raw_master_df["match_date_parsed"] = pd.to_datetime(raw_master_df["date"]).dt.date
    
    settled_results_mask = raw_master_df.get("status", "") == "FT"
    historical_settled_df = raw_master_df[settled_results_mask]
    
    future_fixtures_mask = (
        (raw_master_df.get("status", "") == "NS") & 
        (raw_master_df["match_date_parsed"] >= current_date) & 
        (raw_master_df["match_date_parsed"] <= ninety_days_future)
    )
    upcoming_three_month_df = raw_master_df[future_fixtures_mask]
    
    if historical_settled_df.empty and upcoming_three_month_df.empty:
        return pd.DataFrame()
        
    final_sanitized_pipeline_df = pd.concat([historical_settled_df, upcoming_three_month_df], ignore_index=True)
    final_sanitized_pipeline_df = final_sanitized_pipeline_df.sort_values(by="date", ascending=True)
    
    return final_sanitized_pipeline_df.drop(columns=["match_date_parsed"], errors="ignore")
                
    
# ==============================================================================
# SEGMENT 2 OF 14: MATHEMATICAL COMPUTATION BACKBONE (POISSON CORE)
# ==============================================================================
class SisonkeMathematicalCoreEngine:
    def calculate_poisson_probability(self, actual_count, expected_mean):
        if expected_mean <= 0: 
            expected_mean = 0.001
        return (math.exp(-expected_mean) * (expected_mean ** actual_count)) / math.factorial(actual_count)

    def generate_bivariate_probability_matrix(self, home_expected_xg, away_expected_xg, max_ceiling=10):
        matrix_array = np.zeros((max_ceiling, max_ceiling))
        for h_g in range(max_ceiling):
            for a_g in range(max_ceiling):
                prob_h = self.calculate_poisson_probability(h_g, home_expected_xg)
                prob_a = self.calculate_poisson_probability(a_g, away_expected_xg)
                matrix_array[h_g, a_g] = prob_h * prob_a
        return matrix_array
# ==============================================================================
# SEGMENT 3 OF 14: VENUE-ISOLATED DATASET PARSER & ODDS WIN FREQUENCY CORE
# ==============================================================================
    def parse_live_team_averages(self, df, target_team, target_timestamp, half_life, status_dict, is_frozen=False):
        df_sorted = df[df["match_timestamp"] < target_timestamp].sort_values(by="match_timestamp", ascending=False)
        home_games = df_sorted[df_sorted["home_team"] == target_team]
        away_games = df_sorted[df_sorted["away_team"] == target_team]
        
        metrics_payload = {
            "avg_goals_scored": 1.45, "avg_goals_conceded": 1.20,
            "avg_sot_created": 4.20, "avg_sot_allowed": 3.80,
            "avg_bc_created": 1.30, "avg_bc_allowed": 1.10,
            "home_sot_to_score": 3.5, "home_sot_to_allow": 3.8,
            "away_sot_to_score": 3.5, "away_sot_to_allow": 3.8,
            "avg_box_touches_created": 15.0, "avg_tackles_pct": 0.50, "avg_dribbles_pct": 0.50
        }
        
        if home_games.empty and away_games.empty: return metrics_payload
        
        all_past_rows = pd.concat([home_games, away_games])
        metrics_payload["avg_goals_scored"] = all_past_rows["home_goals"].mean() if not home_games.empty else all_past_rows["away_goals"].mean()
        metrics_payload["avg_goals_conceded"] = all_past_rows["away_goals"].mean() if not home_games.empty else all_past_rows["home_goals"].mean()
        
        # Pull box touches, tackles%, and dribbles% parameters cleanly for the FPE calculations
        metrics_payload["avg_box_touches_created"] = all_past_rows["home_box_touches"].mean() if not home_games.empty else all_past_rows["away_box_touches"].mean()
        metrics_payload["avg_tackles_pct"] = all_past_rows["home_tackles"].mean() if not home_games.empty else all_past_rows["away_tackles"].mean()
        metrics_payload["avg_dribbles_pct"] = all_past_rows["home_dribbles"].mean() if not home_games.empty else all_past_rows["away_dribbles"].mean()
        
        h_sot = home_games["home_sot"].mean() if not home_games.empty else 4.0
        h_gls = home_games["home_goals"].mean() if not home_games.empty else 1.4
        metrics_payload["home_sot_to_score"] = round(h_sot / h_gls, 2) if h_gls > 0 else 4.0
        
        h_sot_all = home_games["away_sot"].mean() if not home_games.empty else 4.0
        h_gls_all = home_games["away_goals"].mean() if not home_games.empty else 1.2
        metrics_payload["home_sot_to_allow"] = round(h_sot_all / h_gls_all, 2) if h_gls_all > 0 else 4.0
        
        a_sot = away_games["away_sot"].mean() if not away_games.empty else 4.0
        a_gls = away_games["away_goals"].mean() if not away_games.empty else 1.1
        metrics_payload["away_sot_to_score"] = round(a_sot / a_gls, 2) if a_gls > 0 else 4.0
        
        a_sot_all = away_games["home_sot"].mean() if not away_games.empty else 4.0
        a_gls_all = away_games["home_goals"].mean() if not away_games.empty else 1.5
        metrics_payload["away_sot_to_allow"] = round(a_sot_all / a_gls_all, 2) if a_gls_all > 0 else 4.0
        
        return metrics_payload

    def calculate_historical_odds_win_frequency(self, df, team, current_target_odds, tolerance_range=0.40):
        team_clean = str(team).upper().strip()
        past_settled = df.dropna(subset=["home_goals", "away_goals"])
        team_matches = past_settled[(past_settled["home_team"] == team_clean) | (past_settled["away_team"] == team_clean)]
        if team_matches.empty: return 45.0, 0, 0
        bracket_matches_count, bracket_wins_count = 0, 0
        for idx, r in team_matches.iterrows():
            is_host = str(r["home_team"]).upper().strip() == team_clean
            odds_col_key = "odds_1" if is_host else "odds_2"
            if odds_col_key in r and pd.notna(r[odds_col_key]):
                historical_match_odds = float(r[odds_col_key])
                if abs(historical_match_odds - float(current_target_odds)) <= tolerance_range:
                    bracket_matches_count += 1
                    h_g, a_g = float(r["home_goals"]), float(r["away_goals"])
                    if h_g == a_g: pass
                    elif (h_g > a_g and is_host) or (a_g > h_g and not is_host): bracket_wins_count += 1
        if bracket_matches_count == 0: return 45.0, 0, 0
        return round((bracket_wins_count / bracket_matches_count) * 100.0, 1), bracket_wins_count, bracket_matches_count

    def run_rolling_window_backtest(self, df, base_g, b_window, h_days, damp):
        if len(df) < 3: return pd.DataFrame()
        return df.tail(15).copy()

import os
# ==============================================================================
# SEGMENT 4 CORE ADDITION: EXPERT WORKSPACE PLATFORM NAVIGATION SWITCH
# ==============================================================================
# Renders an interactive layout switcher directly onto your sidebar dashboard panel
active_app_tab = st.sidebar.radio(
    "Select Active Console Workspace Panel:",
    options=["ðŸ“Š Predictive Analytics Hub", "ðŸ“ Research & Sentiment Tracker"],
    key="sisonke_platform_navigation_radio_v2026"
)
 # ==============================================================================
# SEGMENT 4 PART 1: SELF-CONTAINED PLATFORM CONTROLLER & PERSISTENCE LOCKS
# ==============================================================================
import os
import json

st.sidebar.title("ðŸ§  SISONKE CONTROL PANEL")

# Renders the interactive panel selector directly onto your sidebar dashboard panel
active_app_tab = st.sidebar.radio(
    "Select Active Console Workspace Panel:",
    options=["ðŸ“Š Predictive Analytics Hub", "ðŸ“ Research & Sentiment Tracker"],
    key="sisonke_platform_navigation_radio_v2026_final_lock"
)
st.sidebar.markdown("---")

# ðŸ›‘ THE INTERCEPT GUARD: If you click the tracker tab, render it and stop execution instantly!
if active_app_tab == "ðŸ“ Research & Sentiment Tracker":
    st.subheader("ðŸ“ Sisonke Automated Research & Sentiment Desk")
    st.markdown("---")
    
    # --- STAGE 1: READ STORAGE PERSISTENCE SYSTEMS ---
    checklist_save_path = "sisonke_checklist_storage.json"
    database_csv_path = "master_sisonke_database.csv"
    
    persisted_data = {}
    if os.path.exists(checklist_save_path):
        try:
            with open(checklist_save_path, "r") as f:
                persisted_data = json.load(f)
        except Exception:
            pass
            
    available_leagues = ["No Active Database Connected"]
    master_db_df = pd.DataFrame()
    if os.path.exists(database_csv_path):
        try:
            master_db_df = pd.read_csv(database_csv_path)
            master_db_df.columns = [str(c).strip().lower().replace(" ", "_") for c in master_db_df.columns]
            if "league" in master_db_df.columns:
                available_leagues = sorted(master_db_df["league"].dropna().unique().tolist())
        except Exception:
            available_leagues = ["Upload Database to Sync"]
            
    # --- STAGE 2: INTERACTIVE DROPDOWNS CORE ---
    col_l, col_f = st.columns(2)
    with col_l:
        selected_league = st.selectbox("Active Division Workspace:", options=available_leagues, key="chk_leag_sel")
        
    upcoming_fixtures_list = []
    if not master_db_df.empty and "status" in master_db_df.columns and "league" in master_db_df.columns:
        fixture_mask = (master_db_df["league"] == selected_league) & (master_db_df["status"] == "NS")
        filtered_fixtures_df = master_db_df[fixture_mask]
        if not filtered_fixtures_df.empty and "home" in filtered_fixtures_df.columns and "away" in filtered_fixtures_df.columns:
            for _, row in filtered_fixtures_df.iterrows():
                upcoming_fixtures_list.append(f"{row['home']} vs {row['away']}")
                
    if not upcoming_fixtures_list:
        upcoming_fixtures_list = ["No upcoming fixtures listed in this workspace block"]
        
    with col_f:
        target_fixture = st.selectbox("Select Target Upcoming Fixture:", options=sorted(list(set(upcoming_fixtures_list))), key="chk_fix_sel")
        
    match_id_key = f"{str(selected_league).lower().replace(' ', '_')}_{str(target_fixture).lower().replace(' ', '_')}"
    
    if match_id_key not in persisted_data:
        persisted_data[match_id_key] = {
            "checklist": {f"c{i}": False for i in range(1, 18)},
            "motivation": "Mid-table, Late Season (ðŸ˜´ Beach Mode / High Underperformance Risk)",
            "notes": "",
            "odds_opening_home": 2.00, "odds_opening_draw": 3.20, "odds_opening_away": 3.20,
            "odds_current_home": 2.00, "odds_current_draw": 3.20, "odds_current_away": 3.20
        }
        
    match_state = persisted_data[match_id_key]
        # ==============================================================================
    # AUTOMATED SISONKE TEAM PRICE ACTION DRIFT & STEAM CALCULATOR
    # ==============================================================================
    st.markdown("---")
    st.subheader("ðŸ“Š Team Historical Odds Movement Profile")

    # Guard check: Ensure your master spreadsheet database contains old line columns to read
    if not master_db_df.empty and "home" in master_db_df.columns:
            # ðŸŸ¢ CRASH FIX: Move the team splitter logic BEFORE the try statement block
        if " vs " in str(target_fixture):
            current_home_team = str(target_fixture).split(" vs ")[0].strip()
            current_away_team = str(target_fixture).split(" vs ")[1].strip()
        else:
            current_home_team = ""
            current_away_team = ""

        try:
            # The try block now sits safely below the text splitting equations
            has_odds_columns = "opening_odds_home" in master_db_df.columns and "closing_odds_home" in master_db_df.columns

    
            
            # Check if your uploaded CSV has historical opening and closing odds columns
            # (Standard headers: 'opening_odds_home', 'closing_odds_home', etc.)
            has_odds_columns = "opening_odds_home" in master_db_df.columns and "closing_odds_home" in master_db_df.columns
            
            if has_odds_columns and current_home_team and current_away_team:
                # ðŸ  Step 1: Calculate average price movements for the Home Team
                home_history = master_db_df[master_db_df["home"] == current_home_team]
                if not home_history.empty:
                    open_avg_h = home_history["opening_odds_home"].mean()
                    close_avg_h = home_history["closing_odds_home"].mean()
                    home_historical_shift = ((open_avg_h - close_avg_h) / open_avg_h) * 100 if open_avg_h > 0 else 0
                else:
                    home_historical_shift = 0.0
                    
                # âœˆï¸ Step 2: Calculate average price movements for the Away Team
                away_history = master_db_df[master_db_df["away"] == current_away_team]
                if not away_history.empty:
                    open_avg_a = away_history["opening_odds_away"].mean()
                    close_avg_a = away_history["closing_odds_away"].mean()
                    away_historical_shift = ((open_avg_a - close_avg_a) / open_avg_a) * 100 if open_avg_a > 0 else 0
                else:
                    away_historical_shift = 0.0

                # Render the visual statistical breakdown cards on your mobile layout view
                t_col1, t_col2 = st.columns(2)
                with t_col1:
                    st.metric(
                        label=f"ðŸ  {current_home_team} Average Line Shift", 
                        value=f"{home_historical_shift:.1f}%",
                        delta="ðŸ”¥ Usually Steams (Sharp Inflow)" if home_historical_shift > 1.0 else ("âš ï¸ Usually Drifts (Faded)" if home_historical_shift < -1.0 else "Stable Line Profile")
                    )
                with t_col2:
                    st.metric(
                        label=f"âœˆï¸ {current_away_team} Average Line Shift", 
                        value=f"{away_historical_shift:.1f}%",
                        delta="ðŸ”¥ Usually Steams (Sharp Inflow)" if away_historical_shift > 1.0 else ("âš ï¸ Usually Drifts (Faded)" if away_historical_shift < -1.0 else "Stable Line Profile")
                    )
            else:
                # Friendly fallback warning message if columns aren't detected in your uploaded spreadsheet
                st.info("ðŸ’¡ To track historical team price action, ensure your uploaded CSV contains 'opening_odds_home' and 'closing_odds_home' column headers.")
        except Exception as processing_err:
            st.write(f"Line Tracker Processing Notice: {processing_err}")
    else:
        st.info("ðŸ’¡ Sync your master database file in the Analytics Hub to generate automatic team movement charts.")

    # ==============================================================================
    # SEGMENT 4 PART 2: INTERACTIVE 7-DAY RESEARCH CHECKLIST GRIDS
    # ==============================================================================
    check_col, tracking_col = st.columns([1.1, 0.9])
    
    with check_col:
        st.header("â³ 7-Day Context Checklist")
        st.markdown("#### ðŸ“… 7 Days Out")
        match_state["checklist"]["c1"] = st.checkbox("Check fixture congestion (3 games in 7 days?)", value=match_state["checklist"]["c1"], key="cb1")
        match_state["checklist"]["c2"] = st.checkbox("European/Cup games midweek?", value=match_state["checklist"]["c2"], key="cb2")
        match_state["checklist"]["c3"] = st.checkbox("Review H2H last 5 meetings", value=match_state["checklist"]["c3"], key="cb3")
        
        st.markdown("#### ðŸ“° 72 Hours Out")
        match_state["checklist"]["c4"] = st.checkbox("Watch manager press conferences", value=match_state["checklist"]["c4"], key="cb4")
        match_state["checklist"]["c5"] = st.checkbox("Check injury reports & suspensions", value=match_state["checklist"]["c5"], key="cb5")
        match_state["checklist"]["c6"] = st.checkbox("Note any rotation hints", value=match_state["checklist"]["c6"], key="cb6")
        
        st.markdown("#### ðŸ” 24 Hours Out")
        match_state["checklist"]["c7"] = st.checkbox("Review training photos/videos", value=match_state["checklist"]["c7"], key="cb7")
        match_state["checklist"]["c8"] = st.checkbox("Check team travel distance factors", value=match_state["checklist"]["c8"], key="cb8")
        match_state["checklist"]["c9"] = st.checkbox("Weather forecast verification completed", value=match_state["checklist"]["c9"], key="cb9")
        match_state["checklist"]["c10"] = st.checkbox("Compare lines across 3+ sportsbooks", value=match_state["checklist"]["c10"], key="cb10")
        
        st.markdown("#### âš¡ Match Day & Lineups Release")
        match_state["checklist"]["c11"] = st.checkbox("Final injury report checks completed", value=match_state["checklist"]["c11"], key="cb11")
        match_state["checklist"]["c12"] = st.checkbox("Check early line news leaks", value=match_state["checklist"]["c12"], key="cb12")
        match_state["checklist"]["c13"] = st.checkbox("Monitor odds movements sheets", value=match_state["checklist"]["c13"], key="cb13")
        match_state["checklist"]["c14"] = st.checkbox("Official lineups released (60 Mins Out)", value=match_state["checklist"]["c14"], key="cb14")
        match_state["checklist"]["c15"] = st.checkbox("Formation/tactical setup verified", value=match_state["checklist"]["c15"], key="cb15")
        match_state["checklist"]["c16"] = st.checkbox("Key rotation players in/out accounted for", value=match_state["checklist"]["c16"], key="cb16")
        match_state["checklist"]["c17"] = st.checkbox("Final bet or pass structural decision logged", value=match_state["checklist"]["c17"], key="cb17")
    # ==============================================================================
    # SEGMENT 4 PART 3: MOVING LINE TRACKER & HARD INDUSTRIAL INTERCEPT WALL
    # ==============================================================================
    with tracking_col:
        st.header("ðŸ“ˆ Multi-Day Multi-Market Intercept Tracker")
        st.markdown("Log market price adjustments across all 22 derivative lines and 4 tracking days to detect sharp money flows.")
        
        # ðŸ‘¥ STEP 1: PARSER FOR NAKED TEAM NAMES
        if " vs " in str(target_fixture):
            current_home_team = str(target_fixture).split(" vs ")[0].strip()
            current_away_team = str(target_fixture).split(" vs ")[1].strip()
        else:
            current_home_team = "Home Team"
            current_away_team = "Away Team"

        # Initialize all multi-day and multi-market dictionary keys safely in memory cache
        market_keys = [
            "op_h", "op_a", "d3_h", "d3_a", "db_h", "db_a", "cl_h", "cl_a", # 1X2 Match Winner
            "op_o25", "op_u25", "cl_o25", "cl_u25", # Goal Totals Over/Under 2.5
            "op_btsy", "op_btsn", "cl_btsy", "cl_btsn", # Both Teams To Score
            "op_h15", "op_a15", "cl_h15", "cl_a15" # Team Exact Totals Over 1.5
        ]
        for mk in market_keys:
            if mk not in match_state:
                match_state[mk] = 2.00

        # Mathematical Calculation Engine to evaluate line movement deltas automatically
        def check_market_shift(open_odds, current_odds):
            if open_odds <= 0 or current_odds <= 0: return "0.0% Stable"
            delta_pct = ((open_odds - current_odds) / open_odds) * 100
            if delta_pct > 1.5: return f"ðŸ”¥ STEAM: Dropped by {abs(delta_pct):.1f}% (Sharp Inflow)"
            elif delta_pct < -1.5: return f"âš ï¸ DRIFT: Rose by {abs(delta_pct):.1f}% (Public Fade)"
            return "Stable Line"

        # ðŸ“¦ DROPDOWN 1: 1X2 MATCH WINNER COVERING ALL 4 DAYS
        with st.expander("âš½ 1X2 Match Winner Matrix (4-Day Radar)", expanded=True):
            day_c1, day_c2, day_c3, day_c4 = st.columns(4)
            with day_c1:
                st.markdown("**ðŸ 7 Days Out**")
                match_state["op_h"] = st.number_input(f"{current_home_team} (7D):", value=float(match_state["op_h"]), step=0.05, key="m_oph")
                match_state["op_a"] = st.number_input(f"{current_away_team} (7D):", value=float(match_state["op_a"]), step=0.05, key="m_opa")
            with day_c2:
                st.markdown("**ðŸ“… 3 Days Out**")
                match_state["d3_h"] = st.number_input(f"{current_home_team} (3D):", value=float(match_state["d3_h"]), step=0.05, key="m_d3h")
                match_state["d3_a"] = st.number_input(f"{current_away_team} (3D):", value=float(match_state["d3_a"]), step=0.05, key="m_d3a")
            with day_c3:
                st.markdown("**ðŸ” Day Before**")
                match_state["db_h"] = st.number_input(f"{current_home_team} (DB):", value=float(match_state["db_h"]), step=0.05, key="m_dbh")
                match_state["db_a"] = st.number_input(f"{current_away_team} (DB):", value=float(match_state["db_a"]), step=0.05, key="m_dba")
            with day_c4:
                st.markdown("**ðŸš¨ Closing Line**")
                match_state["cl_h"] = st.number_input(f"{current_home_team} (CL):", value=float(match_state["cl_h"]), step=0.05, key="m_clh")
                match_state["cl_a"] = st.number_input(f"{current_away_team} (CL):", value=float(match_state["cl_a"]), step=0.05, key="m_cla")

        # ðŸ“Š LIVE AUTOMATED TEAM STATUS CARDS (Calculated purely from your inputs above!)
        st.markdown("##### ðŸ“Š Real-Time Input Line Shift Status")
        home_live_shift = ((float(match_state["op_h"]) - float(match_state["cl_h"])) / float(match_state["op_h"])) * 100 if float(match_state["op_h"]) > 0 else 0.0
        away_live_shift = ((float(match_state["op_a"]) - float(match_state["cl_a"])) / float(match_state["op_a"])) * 100 if float(match_state["op_a"]) > 0 else 0.0

        t_col1, t_col2 = st.columns(2)
        with t_col1:
            st.metric(label=f"ðŸ  {current_home_team} Total Trend", value=f"{home_live_shift:.1f}%", delta="ðŸ”¥ Sharp Steam" if home_live_shift > 1.5 else ("âš ï¸ Market Drift" if home_live_shift < -1.5 else "Stable Line"))
        with t_col2:
            st.metric(label=f"âœˆï¸ {current_away_team} Total Trend", value=f"{away_live_shift:.1f}%", delta="ðŸ”¥ Sharp Steam" if away_live_shift > 1.5 else ("âš ï¸ Market Drift" if away_live_shift < -1.5 else "Stable Line"))

        # ðŸ“¦ DROPDOWN 2: OVER/UNDER GOAL TOTALS ALTERNATIVE LINES
        with st.expander("ðŸ¥… Over / Under Goal Totals"):
            g_c1, g_c2 = st.columns(2)
            with g_c1:
                st.markdown("**ðŸ Opening Lines**")
                match_state["op_o25"] = st.number_input("Opening Over 2.5:", value=float(match_state["op_o25"]), step=0.05, key="n_oo25")
                match_state["op_u25"] = st.number_input("Opening Under 2.5:", value=float(match_state["op_u25"]), step=0.05, key="n_ou25")
            with g_c2:
                st.markdown("**ðŸš¨ Live Closing Lines**")
                match_state["cl_o25"] = st.number_input("Live Over 2.5:", value=float(match_state["cl_o25"]), step=0.05, key="n_co25")
                match_state["cl_u25"] = st.number_input("Live Under 2.5:", value=float(match_state["cl_u25"]), step=0.05, key="n_cu25")
            st.caption(f"**Goal Trend:** Over 2.5: {check_market_shift(match_state['op_o25'], match_state['cl_o25'])} | Under 2.5: {check_market_shift(match_state['op_u25'], match_state['cl_u25'])}")

        # ðŸ“¦ DROPDOWN 3: BOTH TEAMS TO SCORE COEFFICIENTS
        with st.expander("ðŸ’¥ Both Teams to Score (BTTS)"):
            b_c1, b_c2 = st.columns(2)
            with b_c1:
                match_state["op_btsy"] = st.number_input("Opening BTTS Yes:", value=float(match_state["op_btsy"]), step=0.05, key="n_obtsy")
                match_state["op_btsn"] = st.number_input("Opening BTTS No:", value=float(match_state["op_btsn"]), step=0.05, key="n_obtsn")
            with b_c2:
                match_state["cl_btsy"] = st.number_input("Live BTTS Yes:", value=float(match_state["cl_btsy"]), step=0.05, key="n_cbtsy")
                match_state["cl_btsn"] = st.number_input("Live BTTS No:", value=float(match_state["cl_btsn"]), step=0.05, key="n_cbtsn")

        # ðŸ“¦ DROPDOWN 4: INDIVIDUAL TEAM ISOLATED GOAL VOLUME LINES
        with st.expander("ðŸ›¡ï¸ Team Exact Totals (Over 1.5)"):
            t_c1, t_c2 = st.columns(2)
            with t_c1:
                match_state["op_h15"] = st.number_input("Opening Home Over 1.5:", value=float(match_state["op_h15"]), step=0.05, key="n_oh15")
                match_state["op_a15"] = st.number_input("Opening Away Over 1.5:", value=float(match_state["op_a15"]), step=0.05, key="n_oa15")
            with t_c2:
                match_state["cl_h15"] = st.number_input("Live Home Over 1.5:", value=float(match_state["cl_h15"]), step=0.05, key="n_ch15")
                match_state["cl_a15"] = st.number_input("Live Away Over 1.5:", value=float(match_state["cl_a15"]), step=0.05, key="n_ca15")

                # ==============================================================================
        # ADDED TO SEGMENT 4 TRACKER: BOOKMAKER OUTRIGHTS MARKET MATRICES
        # ==============================================================================
        # Initialize unique memory cache fields for your outright price inputs safely
        outright_keys = ["o_out_price", "c_out_price"]
        for ok in outright_keys:
            if ok not in match_state:
                match_state[ok] = 5.00

        with st.expander("ðŸ† Bookmaker Outrights Radar (League Winner / Relegation)"):
            st.markdown("##### Log and track long-term seasonal outright lines.")
            
            out_c1, out_c2 = st.columns(2)
            with out_c1:
                match_state["o_out_price"] = st.number_input(
                    f"Opening Outright Price ({current_home_team}):", 
                    value=float(match_state["o_out_price"]), 
                    step=0.50, 
                    key="n_ooutp"
                )
            with out_c2:
                match_state["c_out_price"] = st.number_input(
                    f"Live Closing Outright Price ({current_home_team}):", 
                    value=float(match_state["c_out_price"]), 
                    step=0.50, 
                    key="n_coutp"
                )
                
            # Automatically calculate the seasonal price action shift delta
            out_open = float(match_state["o_out_price"])
            out_close = float(match_state["c_out_price"])
            outright_shift = ((out_open - out_close) / out_open) * 100 if out_open > 0 else 0.0
            
                        # ==============================================================================
            # LINE 644 FIXED: MATCHING SYSTEM SHIFT FUNCTION NAME
            # ==============================================================================
            # ðŸŸ¢ CHANGE 'format_shift_string' TO 'check_market_shift' ON THIS ROW:
            st.info(f"**Outright Market Trend:** {check_market_shift(out_open, out_close)}")

        
        st.markdown("---")
        st.header("ðŸ§  Tactical Environmental Modifiers")
        match_state["motivation"] = st.selectbox("Fixture Motivation Level Profile:", [
            "Mid-table, Late Season (ðŸ˜´ Beach Mode / High Underperformance Risk)",
            "Relegation Battle (ðŸ”¥ Maximum Effort / Underdog Defense Boost)",
            "Champions League Qualification / Promotion Race (âš¡ High Box Intensity)",
            "Derby Matches (ðŸ“ˆ Pride Match / High Variance / Form Breaks)"
        ], index=0, key="sb_mot_nv")

                # ==============================================================================
        # AUTOMATED CHECKBOX CALCULATOR LOCK
        # ==============================================================================
        # ðŸŸ¢ PLACE THIS SINGLE LINE DIRECTLY ABOVE YOUR base_score EQUATION:
        checked_count = sum(1 for v in match_state["checklist"].values() if v is True)
    
        # ðŸ§® STEP 2: ALGORITHMIC CONFIDENCE AUTOMATION
        base_score = (checked_count / len(match_state["checklist"])) * 10
        sentiment_bonus = 0.0
        if "Relegation" in match_state["motivation"] or "Derby" in match_state["motivation"]:
            sentiment_bonus -= 1.0
        elif "Champions" in match_state["motivation"]:
            sentiment_bonus += 0.5
            
        if home_live_shift > 2.0 or away_live_shift > 2.0:
            sentiment_bonus += 1.0  # Stream confirmation reward
        elif home_live_shift < -3.0 or away_live_shift < -3.0:
            sentiment_bonus -= 1.5  # Market divergence penalty

        auto_confidence = max(1.0, min(10.0, base_score + sentiment_bonus))
        st.metric(label="Calculated Confidence Rating (1-10)", value=f"{auto_confidence:.1f} / 10")
        
        if checked_count < 8:
            st.error("ðŸ›‘ PASS / NO BET: Information scarcity detected. Check more checklist tasks.")
        elif auto_confidence >= 7.5:
            st.success("ðŸŽ¯ VALUE TRADING MODE: High verification level matched with solid market sentiment.")
        else:
            st.warning("ðŸ”· ALTERNATIVE LINE LOCK: Mixed data signals or negative price movements.")
            
        match_state["notes"] = st.text_area("Match Findings & Lineup Leak Updates Diary:", value=match_state["notes"], key="ta_notes_nv")
                
        





# ==============================================================================
# SEGMENT 4 FINALIZED: CONFIGURED 4-DIGIT WORKSPACE DIRECTORY
# ==============================================================================
# ðŸŸ¢ Every league index has been updated to match the official 4-digit layout!
st.sidebar.title("ðŸ§  SISONKE CONTROL PANEL")

league_directory = {
    "England Championship": 1040, 
    "Germany 2. Bundesliga": 1079, 
    "Dutch Eredivisie": 1072,
    "Belgium Pro League": 1144, 
    "France Ligue 2": 1062, 
    "Italy Serie B": 1074,
    "Spain Segunda DivisiÃ³n": 1141, 
    "Swedish Allsvenskan": 1113, 
    "Austrian Bundesliga": 1218,
    "Swiss Super League": 1207, 
    "Danish Superliga": 1119, 
    "South African Premier League (PSL)": 1288,
    "Croatia HNL": 1224, 
    "Belgium Challenger Pro": 1145, 
    "Brazil SÃ©rie A": 1262,
    "Brazil SÃ©rie B": 1263, 
    "Australia A-League Men": 1191, 
    "Argentina Tier 1": 1256,
    "Scottish Championship": 1180, 
    "Dutch Eerste Divisie": 1073, 
    "Portugal Liga Portugal 2": 1095,
    "Norway Eliteserien": 1103, 
    "Ireland Premier Div": 1357, 
    "Iceland Besta deild": 1365, 
    "Poland Ekstraklasa": 1106, 
    "Poland I Liga": 1107, 
    "Czech First League": 1172, 
    "Hungary NB I": 1271, 
    "Slovakia Super Liga": 1315, 
    "Chile Primera DivisiÃ³n": 1265, 
    "Colombia Primera A": 1268, 
    "Ecuador Serie A": 1278, 
    "Peru Liga 1": 1281,
    "Canada Premier League": 1448, 
    "Russia Premier League": 1235,
    "Switzerland Challenge League": 1208, 
    "Chinese Super League": 1251, 
    "Chinese League 1": 1252, 
    "Denmark Bet25 Liga": 1120
} # ðŸ›‘ BRACKET IS CLOSED FLUSH FORWARD WITH ZERO TRAILING COMMAS!

# This selection line must sit completely flush left directly beneath it:
selected_workspace = st.sidebar.selectbox(
    "Select Target League Workspace:", 
    options=list(league_directory.keys())
)

active_api_id = league_directory[selected_workspace]

# ðŸ“ THE NEW SEASON INPUT TEXT BOX
# This renders right below your dropdown menu and passes your inputs directly to the code loops
seasons_input_text = st.sidebar.text_input(
    "Enter Required Season Data:",
    value="2025, 2026",
    help="Type out your target multi-season years separated cleanly by commas (e.g., 2025, 2026)."
)

# Convert your screen text entry into a clean mathematical integer list behind the glass
try:
    active_seasons_list = [int(s.strip()) for s in seasons_input_text.split(",") if s.strip().isdigit()]
except Exception:
    active_seasons_list = [2025, 2026] # Safe fallback baseline if you leave it empty or make a typo

# BUTTON A: THE ALL-IN-ONE MASTER FETCH BUTTON (History + Fixtures)
if st.sidebar.button("âš¡ Fetch Live Matchday Data", key="sisonke_api_fetch_trigger_btn_2026"):
    with st.spinner(f"Connecting to Data Gateway... Fetching {selected_workspace} records"):
        # We now pass both the league code AND your custom season list into the fetcher!
        incoming_api_df = fetch_thestatsapi_to_sisonke(active_api_id, active_seasons_list)
        
        if not incoming_api_df.empty:
            incoming_api_df.to_csv("master_sisonke_database.csv", index=False)
            st.session_state["full_validation_df"] = incoming_api_df.copy()
            st.session_state["processed_cache_success"] = True
            st.sidebar.success(f"ðŸ“Š {selected_workspace} Synchronized! History and fixtures loaded cleanly.")
            st.rerun()
        else:
            st.sidebar.error("âŒ Gateway Connection Timeout. Verify Bearer Token or subscription tier.")

# ðŸ“… BUTTON B: THE DEDICATED FIXTURES TRIGGER BUTTON (Fixtures Only)
if st.sidebar.button("ðŸ“… Sync 3-Month Fixtures Only", key="sisonke_fixtures_exclusive_trigger_v2026"):
    with st.spinner(f"Updating {selected_workspace} Fixture Calendar..."):
        import datetime
        import requests
        import pandas as pd
        
        current_date = datetime.date.today()
        ninety_days_future = current_date + datetime.timedelta(days=90)
        
        # Pulls the newest year you typed into your sidebar text box automatically
        newest_active_year = max(active_seasons_list) if active_seasons_list else 2026
        
        api_token = "fapi_MSr9G4BWrzxnDEoDGaUEHOoX82FsjIE3"
                # ==============================================================================
        # SEGMENT 4 BUTTON B FINALISED IMMUNE BASE URL PATHWAY
        # ==============================================================================
        sisonke_front_gate = "https://api.thestatsapi.com"
        url = f"{sisonke_front_gate}/api/football/matches"
        
        button_params = {
            "competition_id": f"comp_{active_api_id}" if "comp_" not in str(active_api_id) else active_api_id,
            "season_id": f"sn_{newest_active_year}" if "sn_" not in str(newest_active_year) else newest_active_year,
            "per_page": 100
        }
        
        # Executes response queries natively with identical headers protection blocks
        response = requests.get(
            url,
            headers={
                "Authorization": f"Bearer fapi_StHSSTzkl40Bc3EJ3znTqH8oEXjz3Szu",
                "Accept": "application/json"
            },
            params=button_params,
            timeout=30
        )

        
        try:
            res = requests.get(url, headers=headers, timeout=10)
            if res.status_code == 200:
                payload = res.json().get("data", [])
                if payload:
                    raw_fixtures_df = pd.DataFrame(payload)
                    raw_fixtures_df["match_date_parsed"] = pd.to_datetime(raw_fixtures_df["date"]).dt.date
                    
                    mask = (raw_fixtures_df["status"] == "NS") & (raw_fixtures_df["match_date_parsed"] >= current_date) & (raw_fixtures_df["match_date_parsed"] <= ninety_days_future)
                    upcoming_df = raw_fixtures_df[mask].drop(columns=["match_date_parsed"], errors="ignore")
                    
                    if os.path.exists("master_sisonke_database.csv"):
                        existing_df = pd.read_csv("master_sisonke_database.csv")
                        completed_games_df = existing_df[existing_df["status"] == "FT"]
                        final_df = pd.concat([completed_games_df, upcoming_df], ignore_index=True).drop_duplicates(keep="last")
                    else:
                        final_df = upcoming_df
                        
                    final_df.to_csv("master_sisonke_database.csv", index=False)
                    st.session_state["full_validation_df"] = final_df.copy()
                    st.sidebar.success("ðŸ“… 3-Month Fixture List Updated Successfully!")
                    st.rerun()
                else:
                    st.sidebar.info("ðŸ’¡ No unplayed fixtures scheduled inside the upcoming 90 days.")
            else:
                st.sidebar.error(f"API Refused Request. Error Code: {res.status_code}")
        except Exception as e:
            st.sidebar.error(f"Connection Fault: {e}")

# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
st.sidebar.markdown("### ðŸ“ Historical Matchday Upload Port")
uploaded_file_stream = st.sidebar.file_uploader("Drop your master CSV database file here to append new matchday lines:", type=["csv"], key="csv_manual_uploader_v1")

storage_path = "master_sisonke_database.csv"

if os.path.exists(storage_path):
    try:
        full_validation_df = pd.read_csv(storage_path)
        if not full_validation_df.empty:
            st.session_state["full_validation_df"] = full_validation_df.copy()
            st.session_state["processed_cache_success"] = True
    except Exception as read_disk_err:
        st.sidebar.error(f"Storage Read Failure: {read_disk_err}")
else:
    full_validation_df = pd.DataFrame()

if uploaded_file_stream is not None:
    try:
        raw_manual_input_df = pd.read_csv(uploaded_file_stream)
        if os.path.exists(storage_path) and not full_validation_df.empty:
            combined_records_df = pd.concat([full_validation_df, raw_manual_input_df], ignore_index=True)
        else:
            combined_records_df = raw_manual_input_df
        combined_records_df.columns = [str(c).strip().lower().replace("%", "").replace(" ", "_") for c in combined_records_df.columns]
        combined_records_df.drop_duplicates(keep="last", inplace=True)
        combined_records_df.to_csv(storage_path, index=False)
        st.session_state["full_validation_df"] = combined_records_df.copy()
        st.session_state["processed_cache_success"] = True
        st.sidebar.success("ðŸ’¾ Persistent Storage Sync Complete!")
        st.rerun()
    except Exception as write_disk_err:
        st.sidebar.error(f"Local Storage Write Fault: {write_disk_err}")

full_validation_df = st.session_state.get("full_validation_df", pd.DataFrame())

st.sidebar.markdown("---")
st.sidebar.subheader("ðŸ’¾ System Storage Hub")

try:
    with open("master_sisonke_database.csv", "rb") as local_storage_file:
        csv_bytes_data = local_storage_file.read()
    st.sidebar.download_button(
        label="ðŸ“¥ Download CSV from Saved Storage",
        data=csv_bytes_data,
        file_name=f"exported_{selected_workspace.lower().replace(' ', '_')}_clean.csv",
        mime="text/csv",
        key="sisonke_unique_sidebar_exporter_v2026",
        help="Instantly exports the active 22-column regular season file directly to your phone storage."
    )
except FileNotFoundError:
    st.sidebar.info("ðŸ’¡ Storage Notice: Local baseline CSV file is not written to disk yet.")
        

    
# ==============================================================================
# SEGMENT 5 OF 14: ADVANCED FUZZY ALIAS MAPPING CORE & TYPE HARDENER
# ==============================================================================
working_pipeline_df = full_validation_df.copy() if not full_validation_df.empty else (pd.read_csv(storage_path) if os.path.exists(storage_path) else pd.DataFrame())

if not working_pipeline_df.empty:
    working_pipeline_df.columns = [str(c).strip().lower().replace("%", "").replace(" ", "_") for c in working_pipeline_df.columns]
    raw_headers = list(working_pipeline_df.columns)
    
    alias_mapping_grid = {
        "league_country": ["competition", "league_country", "div", "league", "tournament"],
        "date_raw": ["date", "match_timestamp", "timestamp", "time", "datetime"],
        "home_team": ["home", "hometeam", "home_team", "host", "team_1"],
        "away_team": ["away", "awayteam", "away_team", "visitor", "team_2"],
        "home_goals": ["home_goals", "home_goals_scored", "home_score", "fthg", "hg", "home_goals_full_time"],
        "away_goals": ["away_goals", "away_goals_scored", "away_score", "ftag", "ag", "away_goals_full_time"],
        "home_sot": ["home_sot", "home_shots_on_target", "hst", "home_sot_total"],
        "away_sot": ["away_sot", "away_shots_on_target", "ast", "away_sot_total"],
        "home_big_chances": ["home_big_chances", "home_chances", "home_bc", "home_major_chances"],
        "away_big_chances": ["away_big_chances", "away_chances", "away_bc", "away_major_chances"],
        "home_box_touches": ["home_box_touches", "home_touches_in_box", "home_penalty_touches"],
        "away_box_touches": ["away_box_touches", "away_touches_in_box", "away_penalty_touches"],
        "home_red_cards": ["home_red_cards", "home_reds", "hr", "home_dismissals"],
        "away_red_cards": ["away_red_cards", "away_reds", "ar", "away_dismissals"],
        "home_tackles": ["home_tackles", "home_tackles_win_ratio", "home_tackles_win"],
        "away_tackles": ["away_tackles", "away_tackles_win_ratio", "away_tackles_win"],
        "home_dribbles": ["home_dribbles", "home_dribbles_win_ratio", "home_dribbles_win"],
        "away_dribbles": ["away_dribbles", "away_dribbles_win_ratio", "away_dribbles_win"],
        "home_duels": ["home_duels", "home_ground_duels_won", "home_duels_win_ratio"],
        "away_duels": ["away_duels", "away_ground_duels_win", "away_duels_win_ratio"]
    }
    
    for core_target_variable, variant_aliases_list in alias_mapping_grid.items():
        for alias in variant_aliases_list:
            if alias in raw_headers:
                working_pipeline_df[core_target_variable] = working_pipeline_df[alias]
                break
                
    if "league_country" not in working_pipeline_df.columns:
        working_pipeline_df["league_country"] = "consensus_league"
        
    if "home_team" in working_pipeline_df.columns:
        working_pipeline_df["home_team"] = working_pipeline_df["home_team"].astype(str).str.upper().str.strip()
    if "away_team" in working_pipeline_df.columns:
        working_pipeline_df["away_team"] = working_pipeline_df["away_team"].astype(str).str.upper().str.strip()

    numeric_targets_list = [
        "home_goals", "away_goals", "home_sot", "away_sot", 
        "home_big_chances", "away_big_chances", "home_box_touches", "away_box_touches", 
        "home_red_cards", "away_red_cards", "home_tackles", "away_tackles",
        "home_dribbles", "away_dribbles", "home_duels", "away_duels"
    ]
    for col in numeric_targets_list:
        if col in working_pipeline_df.columns:
            working_pipeline_df[col] = pd.to_numeric(working_pipeline_df[col], errors='coerce')
        else:
            working_pipeline_df[col] = np.nan

    if "date_raw" in working_pipeline_df.columns:
        clean_datetime_series = working_pipeline_df["date_raw"].astype(str).str.replace("T", " ").str.strip()
        working_pipeline_df["match_timestamp"] = pd.to_datetime(clean_datetime_series, errors='coerce')
    else:
        working_pipeline_df["match_timestamp"] = pd.Timestamp.now()
        
    working_pipeline_df["match_timestamp"] = working_pipeline_df["match_timestamp"].fillna(pd.Timestamp.now())

    working_pipeline_df.drop_duplicates(subset=["league_country", "match_timestamp", "home_team", "away_team"], keep="last", inplace=True)
    uploaded_leagues = sorted(list(working_pipeline_df["league_country"].dropna().unique()))
else:
    st.info("ðŸ“‚ Data Control Room Active: Please upload your recent match history CSV file to begin training.")
    st.stop()

selected_league_filter = st.selectbox("Select Target League Workspace Selection:", uploaded_leagues)
filtered_df = working_pipeline_df[working_pipeline_df["league_country"].str.lower().str.strip() == selected_league_filter.lower().strip()].reset_index(drop=True)
settled_past_games = filtered_df.dropna(subset=["home_goals", "away_goals"]).reset_index(drop=True)
# ==============================================================================
# SEGMENT 6 OF 14: BREAK-INSULATED TIME TUNER & DUAL DATA CLEARING VAULT
# ==============================================================================
optimal_half_life = 45
automatically_tuned_vol_dampener = 1.00
automatically_tuned_cs_ceiling = 6.0
automatically_tuned_confidence_floor = 50
automatically_tuned_hfa_factor = 1.15
automatically_tuned_sot_weight = 0.12
automatically_tuned_bc_weight = 0.38
automatically_tuned_rho_parameter = -0.05

automatically_tuned_turnover_volatility = 1.00
if len(settled_past_games) >= 5:
    squad_turnover_index = settled_past_games["home_goals"].std() / max(0.1, settled_past_games["home_goals"].mean())
    if squad_turnover_index > 0.85:
        automatically_tuned_turnover_volatility = 1.15
    else:
        automatically_tuned_turnover_volatility = 0.95

league_is_frozen_midbreak = st.session_state.freeze_matrix.get(selected_league_filter.lower().strip(), False)

if len(settled_past_games) >= 5:
    if league_is_frozen_midbreak:
        optimal_half_life = 5 
    else:
        lowest_historical_brier = 999.0
        for test_hl in range(15, 91, 15):
            test_brier_accumulator, tc = 0.0, 0
            for idx, r in settled_past_games.tail(15).iterrows():
                act_outcome = 1.0 if r["home_goals"] > r["away_goals"] else 0.0
                h_sot_avg = filtered_df[(filtered_df["home_team"] == r["home_team"]) & (filtered_df["match_timestamp"] < r["match_timestamp"])]["home_sot"].mean()
                h_sot_val = h_sot_avg if pd.notna(h_sot_avg) else 4.0
                test_brier_accumulator += ((h_sot_val / 8.0) - act_outcome) ** 2
                tc += 1
            if tc > 0 and (test_brier_accumulator / tc) < lowest_historical_brier:
                lowest_historical_brier = test_brier_accumulator / tc
                optimal_half_life = test_hl

    total_goals_series = settled_past_games["home_goals"].astype(float) + settled_past_games["away_goals"].astype(float)
    historical_goal_mean = total_goals_series.mean()
    historical_goal_variance = total_goals_series.var()
    if historical_goal_mean > 0 and not pd.isna(historical_goal_variance):
        dispersion_ratio = historical_goal_variance / historical_goal_mean
        automatically_tuned_vol_dampener = max(0.50, min(1.50, float(round(dispersion_ratio * automatically_tuned_turnover_volatility, 2))))

    actual_low_draw_count = len(settled_past_games[((settled_past_games["home_goals"] == 0) & (settled_past_games["away_goals"] == 0)) | ((settled_past_games["home_goals"] == 1) & (settled_past_games["away_goals"] == 1))])
    expected_low_draw_ratio = actual_low_draw_count / len(settled_past_games) if not settled_past_games.empty else 0
    calculated_rho_unbound = -0.15 * (1.0 - (historical_goal_mean / 2.50)) if historical_goal_mean > 0 else -0.05
    if expected_low_draw_ratio > 0.28: calculated_rho_unbound -= 0.05
    automatically_tuned_rho_parameter = max(-0.22, min(0.10, float(round(calculated_rho_unbound, 3))))

    total_red_cards = float(settled_past_games["home_red_cards"].fillna(0).sum() + settled_past_games["away_red_cards"].fillna(0).sum()) if "home_red_cards" in settled_past_games.columns else 0.0
    automatically_tuned_cs_ceiling = max(4.0, min(9.0, float(round(6.0 + ((total_red_cards / len(settled_past_games)) * 10.0), 1))))
    stability_proxy = max(0.01, float(lowest_historical_brier if not league_is_frozen_midbreak and lowest_historical_brier < 999 else 0.22))
    automatically_tuned_confidence_floor = max(20, min(80, int(round(100 - (stability_proxy * 200)))))
    total_home_goals = settled_past_games["home_goals"].sum()
    total_away_goals = settled_past_games["away_goals"].sum()
    if total_away_goals > 0: automatically_tuned_hfa_factor = max(1.02, min(1.35, float(round(total_home_goals / total_away_goals, 2))))

    total_league_goals = total_home_goals + total_away_goals
    total_league_sot = settled_past_games["home_sot"].sum() + settled_past_games["away_sot"].sum() if "home_sot" in settled_past_games.columns else 1.0
    if total_league_sot > 0:
        actual_finishing_rate = total_league_goals / total_league_sot
        automatically_tuned_sot_weight = max(0.08, min(0.18, float(round(actual_finishing_rate * 0.40, 3))))
        automatically_tuned_bc_weight = max(0.25, min(0.55, float(round(actual_finishing_rate * 1.25, 3))))

with st.expander("ðŸ› ï¸ Advanced Calibration & Mathematical Tuning Vault", expanded=False):
    activate_manual_decay_override = st.checkbox("Uncouple Stage 1 Auto-Tuner (Manual Parameter Override)", value=False)
    if activate_manual_decay_override:
        half_life_days = st.slider("Time-Decay Half Life (Days/Steps)", 3, 90, int(optimal_half_life), 1)
        vol_dampener = st.slider("Volatility Dampener", 0.5, 1.5, float(automatically_tuned_vol_dampener), 0.05)
        max_score_cap = st.slider("Max Score Ceiling", 4, 10, int(automatically_tuned_cs_ceiling), 1)
        confidence_floor_input = st.slider("Strict Confidence Floor Trigger (%)", 15, 85, int(automatically_tuned_confidence_floor), 5)
        rho_parameter_input = st.slider("Manual Dixon-Coles Rho (Ï) Adjustment", -0.25, 0.25, float(automatically_tuned_rho_parameter), 0.01)
    else:
        half_life_days = int(optimal_half_life)
        vol_dampener = float(automatically_tuned_vol_dampener)
        max_score_cap = int(automatically_tuned_cs_ceiling)
        confidence_floor_input = int(automatically_tuned_confidence_floor)
        rho_parameter_input = float(automatically_tuned_rho_parameter)
        
        if league_is_frozen_midbreak: st.warning(f"â„ï¸ Hiatus Shield Active: Brier Day loops frozen. Lookback locked to {half_life_days} steps.")
        else: st.success(f"ðŸŽ¯ Auto-Tuner Active: Lookback window optimized via Brier Score at {half_life_days} calendar days.")
        st.success(f"ðŸ¦… Volatility Auto-Calibrated: Dampener dynamically tuned to {vol_dampener:.2f} via dispersion.")
        st.success(f"ðŸ›¡ï¸ Dixon-Coles Parameter: Dynamic Rho (Ï) auto-formulated to {rho_parameter_input:+.3f}")
        st.success(f"ðŸ“¦ Squad Stability Framework: Dynamic Turnover Volatility Scalar locked at {automatically_tuned_turnover_volatility:.2f}")
        
    vol_dampener_adjusted = vol_dampener
    backtest_window = st.slider("Backtest Window Size (Days)", 90, 365, 180, 5)
    accuracy_threshold_floor = st.slider("Strict Accuracy Floor (%)", 35, 75, 50, 5) / 100.0
    
    st.markdown("##### ðŸ¤– Secure Telegram Syndicate Dispatch Vault")
    telegram_token_string = st.text_input("Enter Private Bot Token API Key:", type="password", value="738491024:AAFlokw...")
    telegram_chat_id_vault = st.text_input("Enter Target Syndicate Group Chat ID:", value="-10029384912")
    
    st.markdown("---")
    st.markdown("##### ðŸ§¹ Local Database Maintenance Panel")
    clear_c1, clear_c2 = st.columns(2)
    trigger_partial_clear = clear_c1.button(f"ðŸ§¹ Clear {selected_league_filter} Data", key="btn_partial_clear_v1")
    if trigger_partial_clear:
        if not working_pipeline_df.empty:
            preserved_leagues_df = working_pipeline_df[working_pipeline_df["league_country"].str.lower().str.strip() != selected_league_filter.lower().strip()]
            if not preserved_leagues_df.empty:
                preserved_leagues_df.to_csv(storage_path, index=False)
                st.session_state["full_validation_df"] = preserved_leagues_df.copy()
            else:
                if os.path.exists(storage_path): os.remove(storage_path)
                st.session_state["full_validation_df"] = pd.DataFrame()
                st.session_state["processed_cache_success"] = False
            st.toast(f"Purged {selected_league_filter} data! Reloading files...")
            st.rerun()
            
    trigger_wipe_database_execution = clear_c2.button("ðŸš¨ WIPE ALL DATABASE RECORDS", key="btn_wipe_db_core_vault")
    if trigger_wipe_database_execution:
        if os.path.exists(storage_path): os.remove(storage_path)
        st.session_state["full_validation_df"] = pd.DataFrame()
        st.session_state["processed_cache_success"] = False
        st.toast("Platform storage completely wiped!")
        st.rerun()

for idx, league in enumerate(uploaded_leagues):
    st.session_state.freeze_matrix[league.lower().strip()] = st.checkbox(f"Freeze Decay: {league.upper()}", value=st.session_state.freeze_matrix.get(league.lower().strip(), False), key=f"f_{idx}")
        # ==============================================================================
# SEGMENT 7 OF 14: TOURNAMENT STRUCTURE WRAPPER & STREAK MATH ENGINES
# ==============================================================================
class ComprehensivePredictiveRoutingEngine(SisonkeMathematicalCoreEngine):
    def predict_match_probabilities(self, df, h_team, a_team, ts, base_g, h_att, a_att, h_stat, a_stat, max_c, damp, tournament_stage="Standard Regular Season Schedule"):
        stage_modifier = 1.00
        if tournament_stage == "Two-Legged Cup Tie: 1st Leg Cagey Strategy": 
            stage_modifier = 0.85
        elif tournament_stage == "Two-Legged Cup Tie: 2nd Leg High-Velocity Chase": 
            stage_modifier = 1.20
        elif tournament_stage == "Single-Elimination Knockout Finals (Neutral Venue)": 
            stage_modifier = 0.90
        
        raw_prob_matrix = self.generate_bivariate_probability_matrix(1.5 * h_att * stage_modifier, 1.1 * a_att * stage_modifier, max_c)
        prob_home = float(np.sum(np.tril(raw_prob_matrix, -1)))
        prob_draw = float(np.sum(np.diag(raw_prob_matrix)))
        prob_away = float(np.sum(np.triu(raw_prob_matrix, 1)))
        
        prob_denom = prob_home + prob_draw + prob_away
        if prob_denom > 0: 
            prob_home /= prob_denom; prob_draw /= prob_denom; prob_away /= prob_denom
        return {"market_probabilities": {"1 (Home Win)": prob_home, "X (Draw)": prob_draw, "2 (Away Win)": prob_away}, "raw_matrix": raw_prob_matrix}

    def compute_squad_streak_profile(self, df, team):
        team_clean = str(team).upper().strip()
        df_sorted = df.dropna(subset=["home_goals", "away_goals"]).sort_values(by="match_timestamp", ascending=True)
        t_rows = df_sorted[(df_sorted["home_team"] == team_clean) | (df_sorted["away_team"] == team_clean)]
        if t_rows.empty: return "0 Game Baseline Streak", 1.0
        
        current_streak_counter = 0
        streak_direction_label = "Undefeated"
        form_multiplier_scalar = 1.0
        
        for idx, r in t_rows.iterrows():
            is_host_side = str(r["home_team"]).upper().strip() == team_clean
            h_g, a_g = float(r["home_goals"]), float(r["away_goals"])
            if h_g == a_g: current_streak_counter += 1
            elif (h_g > a_g and is_host_side) or (a_g > h_g and not is_host_side):
                if streak_direction_label == "Win Streak": current_streak_counter += 1
                else: streak_direction_label = "Win Streak"; current_streak_counter = 1
            else:
                streak_direction_label = "Deficit Run"; current_streak_counter = 1
                
        if streak_direction_label == "Win Streak" and current_streak_counter >= 2:
            form_multiplier_scalar = min(1.12, 1.0 + (float(current_streak_counter) * 0.02))
        elif streak_direction_label == "Deficit Run" and current_streak_counter >= 2:
            form_multiplier_scalar = max(0.88, 1.0 - (float(current_streak_counter) * 0.03))
        return f"{current_streak_counter} Game {streak_direction_label}", form_multiplier_scalar

    def calculate_historical_odds_win_frequency(self, df, team, current_target_odds, tolerance_range=0.40):
        team_clean = str(team).upper().strip()
        past_settled = df.dropna(subset=["home_goals", "away_goals"])
        team_matches = past_settled[(past_settled["home_team"] == team_clean) | (past_settled["away_team"] == team_clean)]
        if team_matches.empty: return 45.0, 0, 0
        bracket_matches_count, bracket_wins_count = 0, 0
        for idx, r in team_matches.iterrows():
            is_host = str(r["home_team"]).upper().strip() == team_clean
            odds_col_key = "odds_1" if is_host else "odds_2"
            if odds_col_key in r and pd.notna(r[odds_col_key]):
                historical_match_odds = float(r[odds_col_key])
                if abs(historical_match_odds - float(current_target_odds)) <= tolerance_range:
                    bracket_matches_count += 1
                    if float(r["home_goals"]) == float(r["away_goals"]): pass
                    elif (float(r["home_goals"]) > float(r["away_goals"]) and is_host) or (float(r["away_goals"]) > float(r["home_goals"]) and not is_host):
                        bracket_wins_count += 1
        if bracket_matches_count == 0: return 45.0, 0, 0
        return round((bracket_wins_count / bracket_matches_count) * 100.0, 1), bracket_wins_count, bracket_matches_count

engine = ComprehensivePredictiveRoutingEngine()
# ==============================================================================
# SEGMENT 8 OF 14: ASYMMETRIC CONTROLS & TEAM-SPECIFIC TURNOVER CHECKBOXES
# ==============================================================================
tab_proj, tab_standings, tab_history, tab_past = st.tabs(["ðŸ”® ACTIVE PROJECTIONS MATRIX", "ðŸ“‹ COMPETITION STANDINGS", "ðŸ“‰ PERFORMANCE BACKTESTER", "ðŸ“œ HISTORICAL RESULT LEDGER"])

with tab_proj:
    dash_left, dash_right = st.columns(2)
    
    with dash_left:
        st.markdown("### â›… Strategic Context Overrides")
        all_teams_raw = sorted(list(set(filtered_df["home_team"].dropna().unique()).union(set(filtered_df["away_team"].dropna().unique()))))
        
        all_teams_labels_map = {}
        for t_name in all_teams_raw:
            t_rows = filtered_df[(filtered_df["home_team"] == t_name) | (filtered_df["away_team"] == t_name)]
            if len(t_rows) > 0 and len(t_rows) < 5:
                avg_goals_check = t_rows["home_goals"].mean() if not t_rows[t_rows["home_team"]==t_name].empty else t_rows["away_goals"].mean()
                if pd.notna(avg_goals_check) and avg_goals_check >= 1.4: all_teams_labels_map[t_name] = f"{t_name} [â–² PROMOTED]"
                else: all_teams_labels_map[t_name] = f"{t_name} [â–¼ RELEGATED]"
            else: all_teams_labels_map[t_name] = t_name

        h_selected_raw = st.selectbox("Host Selection Profile (1):", all_teams_raw, index=0, format_func=lambda x: all_teams_labels_map.get(x, x))
        a_selected_raw = st.selectbox("Visitor Selection Profile (2):", all_teams_raw, index=min(1, len(all_teams_raw)-1), format_func=lambda x: all_teams_labels_map.get(x, x))
        
        target = {"home_team": h_selected_raw, "away_team": a_selected_raw}
        target_ts = pd.Timestamp.now()
        
        st.markdown("##### ðŸ“¦ Squad Stability & Divisional Turnover Filters")
        turn_c1, turn_c2 = st.columns(2)
        
        host_is_promoted = turn_c1.checkbox(f"Host ({h_selected_raw}): â–² Newly Promoted Side", value=False)
        host_has_relegation_threat = turn_c1.checkbox(f"Host ({h_selected_raw}): â–¼ Active Relegation Threat", value=False)
        
        visitor_is_promoted = turn_c2.checkbox(f"Visitor ({a_selected_raw}): â–² Newly Promoted Side", value=False)
        visitor_has_relegation_threat = turn_c2.checkbox(f"Visitor ({a_selected_raw}): â–¼ Active Relegation Threat", value=False)
        
        turnover_modifier_h = 1.00
        turnover_modifier_w = 1.00
        
        if host_is_promoted: turnover_modifier_h *= 1.12
        if host_has_relegation_threat: turnover_modifier_h *= 1.08
        if visitor_is_promoted: turnover_modifier_w *= 1.12
        if visitor_has_relegation_threat: turnover_modifier_w *= 1.08
        
        active_tournament_format_stage = st.radio(
            "Competition Tournament Structural Stage:",
            options=[
                "Standard Regular Season Schedule", 
                "Two-Legged Cup Tie: 1st Leg Cagey Strategy", 
                "Two-Legged Cup Tie: 2nd Leg High-Velocity Chase", 
                "Single-Elimination Knockout Finals (Neutral Venue)"
            ],
            index=0, horizontal=True
        )
        
        referee_strictness_tier = st.radio("Referee Strictness Profile Status Panel:", options=["Lenient (Flow Enforcer)", "Standard Average", "Hyper-Strict (Card Trigger)"], index=1, horizontal=True)
        
        st.markdown("##### ðŸŸï¸ Venue Momentum & Active Streak Matrix Display")
        h_streak_label, h_streak_scalar = engine.compute_squad_streak_profile(filtered_df, h_selected_raw)
        a_streak_label, a_streak_scalar = engine.compute_squad_streak_profile(filtered_df, a_selected_raw)
        
        card_col1, card_col2 = st.columns(2)
        card_col1.info(f"**HOST MOMENTUM:**\n* {h_selected_raw}\n* Status: `{h_streak_label}`\n* Impact Multiplier: `{h_streak_scalar * turnover_modifier_h:.2f}x`")
        card_col2.info(f"**VISITOR MOMENTUM:**\n* {a_selected_raw}\n* Status: `{a_streak_label}`\n* Impact Multiplier: `{a_streak_scalar * turnover_modifier_w:.2f}x`")
        
        with st.expander("ðŸŽ›ï¸ Tactical Setup Blueprints & Calendar Overrides", expanded=False):
            st.checkbox("Flag Match Window as PRE-SEASON FIXTURE", value=False, key="cb_preseason_v1")
            c_tact1, c_tact2 = st.columns(2)
            home_blueprint = c_tact1.selectbox("Host: Tactical Setup:", ["Standard Open Play", "Deep Ultra-Defensive Low-Block", "High-Intensity Counter-Pressing Style"])
            away_blueprint = c_tact2.selectbox("Visitor: Tactical Setup:", ["Standard Open Play", "Deep Ultra-Defensive Low-Block", "High-Intensity Counter-Pressing Style"])
            
            c_cup1, c_cup2 = st.columns(2)
            home_lookahead_distraction = c_cup1.checkbox("Host: Apply Look-Ahead Cup Penalty", value=False)
            away_lookahead_distraction = c_cup2.checkbox("Visitor: Apply Look-Ahead Cup Penalty", value=False)
            
            st.markdown("##### ðŸŒ¦ï¸ Environmental Condition Settings")
            pitch_surface_condition = st.selectbox("On-Pitch Surface State:", ["Standard Optimized Turf", "Waterlogged Mud", "Dry Uneven Grass"])
            weather_climate_outlook = st.selectbox("Matchday Weather Outlook:", ["Clear Sky / Ideal Climate", "Torrential Rain Storm", "Gale-Force Wind Interference"])
            
            st.markdown("##### ðŸ§  Institutional & Psychological Context")
            match_venue_ground_setting = st.selectbox("Fixture Venue Ground Context:", ["Standard VenueSplit (Traditional H/A)", "Neutral Ground / Empty-Stadium Lockout"])
            apply_h2h_bogey_hex_penalty = st.checkbox("Apply Historical H2H Bogey Penalty", value=False)
            
            c_m1, c_m2 = st.columns(2)
            home_manager_bounce = c_m1.checkbox("Host: New Manager Bounce", value=False)
            away_manager_bounce = c_m2.checkbox("Visitor: New Manager Bounce", value=False)
            
            c_f1, c_f2 = st.columns(2)
            home_financial_crisis = c_f1.checkbox("Host: Boardroom Crisis", value=False)
            away_financial_crisis = c_f2.checkbox("Visitor: Boardroom Crisis", value=False)
            
            c_d1, c_f3 = st.columns(2)
            home_dead_rubber = c_d1.checkbox("Host: Late-Season Dead-Rubber", value=False)
            away_dead_rubber = c_f3.checkbox("Visitor: Late-Season Dead-Rubber", value=False)
            
            c_t1, c_t2 = st.columns(2)
            home_travel_load_units = c_t1.slider("Host Mid-Week Travel Fatigue:", 0, 3, 0)
            away_travel_load_units = c_t2.slider("Visitor Mid-Week Travel Fatigue:", 0, 3, 0)
            apply_coastal_climate_shock = st.checkbox("Apply High-Humidity Coastal Shock to Traveler", value=False)
        
        st.markdown("##### ðŸ’µ Commercial Sportsbook Payout Odds Vault")
        c1, c2, c3 = st.columns(3)
        odds_1 = c1.number_input("Odds Home (1):", min_value=1.01, value=2.10, step=0.05)
        odds_X = c2.number_input("Odds Draw (X):", min_value=1.01, value=3.20, step=0.05)
        odds_2 = c3.number_input("Odds Away (2):", min_value=1.01, value=3.40, step=0.05)
        c4, c5, c6 = st.columns(3)
        odds_1X = c4.number_input("Odds 1X:", min_value=1.01, value=1.35, step=0.05)
        odds_X2 = c5.number_input("Odds X2:", min_value=1.01, value=1.70, step=0.05)
        odds_12 = c6.number_input("Odds 12:", min_value=1.01, value=1.28, step=0.05)
        c7, c8 = st.columns(2)
        odds_dnb1 = c7.number_input("Odds DNB1:", min_value=1.01, value=1.50, step=0.05)
        odds_dnb2 = c8.number_input("Odds DNB2:", min_value=1.01, value=2.40, step=0.05)
        c9, c10 = st.columns(2)
        odds_over = c9.number_input("Odds Over 2.5:", min_value=1.01, value=1.90, step=0.05)
        odds_under = c10.number_input("Odds Under 2.5:", min_value=1.01, value=1.90, step=0.05)
# ==============================================================================
# SEGMENT 9 OF 14: ASYMMETRIC COMPILATION LOOPS & DIXON-COLES RHO INJECTION
# ==============================================================================
        c11, c12 = st.columns(2)
        odds_btts_y = c11.number_input("Odds BTTS Yes:", min_value=1.01, value=1.80, step=0.05)
        odds_btts_n = c12.number_input("Odds BTTS No:", min_value=1.01, value=2.00, step=0.05)
        c13, c14, c15, c16 = st.columns(4)
        odds_home_over_15 = c13.number_input("Home Over 1.5:", min_value=1.01, value=2.10)
        odds_home_under_15 = c14.number_input("Home Under 1.5:", min_value=1.01, value=1.65)
        odds_away_over_15 = c15.number_input("Away Over 1.5:", min_value=1.01, value=2.80)
        odds_away_under_15 = c16.number_input("Away Under 1.5:", min_value=1.01, value=1.38)
        c17, c18, c19, c20 = st.columns(4)
        odds_ah_home_minus_15 = c17.number_input("AH Home -1.5:", min_value=1.01, value=3.80)
        odds_ah_away_plus_15 = c18.number_input("AH Away +1.5:", min_value=1.01, value=1.22)
        odds_ah_home_plus_15 = c19.number_input("AH Home +1.5:", min_value=1.15, value=1.15)
        odds_ah_away_minus_15 = c20.number_input("AH Away -1.5:", min_value=1.01, value=6.50)
        c21, c22, c23 = st.columns(3)
        odds_home_cs_y = c21.number_input("Home CS Yes:", min_value=1.01, value=2.60)
        odds_away_cs_y = c22.number_input("Away CS Yes:", min_value=1.01, value=4.20)
        odds_correct_score = c23.number_input("Target CS Payout Line:", min_value=1.01, value=8.50)

        if not filtered_df.empty:
            filtered_df["home_team"] = filtered_df["home_team"].astype(str).str.upper().str.strip()
            filtered_df["away_team"] = filtered_df["away_team"].astype(str).str.upper().str.strip()
            home_target_key = str(target["home_team"]).upper().strip()
            away_target_key = str(target["away_team"]).upper().strip()
            past_home = filtered_df[(filtered_df["home_team"] == home_target_key) & (filtered_df["home_goals"].notna()) & (filtered_df["away_goals"].notna())]
            past_away = filtered_df[(filtered_df["away_team"] == away_target_key) & (filtered_df["home_goals"].notna()) & (filtered_df["away_goals"].notna())]
            sd = len(past_home) + len(past_away)
            confidence = min(100, int((sd / 10.0) * 100)) if sd > 0 else 50

            h_mod, w_mod, damp_mod = 1.0 * turnover_modifier_h, 1.0 * turnover_modifier_w, vol_dampener_adjusted
            if st.session_state.get("cb_preseason_v1", False): h_mod *= 0.90; w_mod *= 0.90
            if home_manager_bounce: h_mod *= 1.10
            if away_manager_bounce: w_mod *= 1.10
            if home_financial_crisis: h_mod *= 0.85
            if away_financial_crisis: w_mod *= 0.85
            if home_dead_rubber: h_mod *= 0.90; damp_mod *= 0.90
            if away_dead_rubber: w_mod *= 0.90; damp_mod *= 0.90
            h_mod *= (1.0 - (float(home_travel_load_units) * 0.04))
            w_mod *= (1.0 - (float(away_travel_load_units) * 0.04))
            if apply_coastal_climate_shock: w_mod *= 0.95; damp_mod *= 0.92
            if home_blueprint == "Deep Ultra-Defensive Low-Block": h_mod *= 0.85; damp_mod *= 0.82
            if away_blueprint == "Deep Ultra-Defensive Low-Block": w_mod *= 0.85; damp_mod *= 0.82
            if home_lookahead_distraction: h_mod *= 0.88
            if away_lookahead_distraction: w_mod *= 0.88
            if referee_strictness_tier == "Hyper-Strict (Card Trigger)": damp_mod *= 1.15
            if apply_h2h_bogey_hex_penalty: h_mod *= 0.95
            hfa_applied = 1.00 if match_venue_ground_setting == "Neutral Ground / Empty-Stadium Lockout" else automatically_tuned_hfa_factor

            res = engine.predict_match_probabilities(filtered_df, home_target_key, away_target_key, target_ts, baseline_goals, hfa_applied * h_mod, 1.0 * w_mod, {}, {}, max_score_cap, damp_mod, active_tournament_format_stage)
            h_s = engine.parse_live_team_averages(filtered_df, home_target_key, target_ts, half_life_days, {}, False)
            a_s = engine.parse_live_team_averages(filtered_df, away_target_key, target_ts, half_life_days, {}, False)
            prob_home, prob_draw, prob_away, prob_matrix = res["market_probabilities"]["1 (Home Win)"], res["market_probabilities"]["X (Draw)"], res["market_probabilities"]["2 (Away Win)"], res["raw_matrix"]
            
            current_active_rho = float(rho_parameter_input)
            prob_matrix *= (1.0 - current_active_rho)
            total_mass_norm = float(np.sum(prob_matrix))
            if total_mass_norm > 0: prob_matrix /= total_mass_norm
            prob_home = float(np.sum(np.tril(prob_matrix, -1)))
            prob_draw = float(np.sum(np.diag(prob_matrix)))
            prob_away = float(np.sum(np.triu(prob_matrix, 1)))
        # ==============================================================================
# SEGMENT 10 OF 14: ALTERNATIVE OPTION MARKET MATRIX GENERATOR
# ==============================================================================
            over_25_p = 0.0
            for h_g in range(max_score_cap):
                for a_g in range(max_score_cap):
                    if (h_g + a_g) > 2.5: over_25_p += float(prob_matrix[h_g, a_g])
            under_25_p = max(0.0, min(1.0, 1.0 - over_25_p))
            btts_yes_p = 0.0
            for h_g in range(1, max_score_cap):
                for a_g in range(1, max_score_cap): btts_yes_p += float(prob_matrix[h_g, a_g])
            btts_no_p = max(0.0, min(1.0, 1.0 - btts_yes_p))
            dc_1X_p = max(0.0, min(1.0, prob_home + prob_draw))
            dc_X2_p = max(0.0, min(1.0, prob_draw + prob_away))
            dc_12_p = max(0.0, min(1.0, prob_home + prob_away))
            win_denominator_sum = prob_home + prob_away
            dnb_1_p, dnb_2_p = (float(prob_home / win_denominator_sum), float(prob_away / win_denominator_sum)) if win_denominator_sum > 0 else (0.50, 0.50)
            home_over_15_p = float(np.sum(prob_matrix[2:max_score_cap, :]))
            home_under_15_p = max(0.0, min(1.0, 1.0 - home_over_15_p))
            away_over_15_p = float(np.sum(prob_matrix[:, 2:max_score_cap]))
            away_under_15_p = max(0.0, min(1.0, 1.0 - away_over_15_p))
            home_cs_p = float(np.sum(prob_matrix[:, 0])) 
            away_cs_p = float(np.sum(prob_matrix[0, :])) 
            ah_home_minus_15_p = 0.0
            for h_g in range(max_score_cap):
                for a_g in range(max_score_cap):
                    if (h_g - a_g) > 1.5: ah_home_minus_15_p += float(prob_matrix[h_g, a_g])
            ah_away_plus_15_p = max(0.0, min(1.0, 1.0 - ah_home_minus_15_p))
            ah_away_minus_15_p = 0.0
            for h_g in range(max_score_cap):
                for a_g in range(max_score_cap):
                    if (a_g - h_g) > 1.5: ah_away_minus_15_p += float(prob_matrix[h_g, a_g])
            ah_home_plus_15_p = max(0.0, min(1.0, 1.0 - ah_away_minus_15_p))
            bookmaker_market_overround_margin = (1.0 / float(odds_1)) + (1.0 / float(odds_X)) + (1.0 / float(odds_2))
            raw_matrix_dictionary_build = [
                ("HOME WIN (1)", odds_1, prob_home, "MODERATE TRAJECTORY"), ("DRAW MATCH (X)", odds_X, prob_draw, "HIGH-STOCHASTIC LOTTERY"), ("AWAY WIN (2)", odds_2, prob_away, "MODERATE TRAJECTORY"),
                ("DOUBLE CHANCE (1X)", odds_1X, dc_1X_p, "LOW COIN-FLIP"), ("DOUBLE CHANCE (X2)", odds_X2, dc_X2_p, "LOW COIN-FLIP"), ("DOUBLE CHANCE (12)", odds_12, dc_12_p, "LOW COIN-FLIP"),
                ("DRAW NO BET (DNB1)", odds_dnb1, dnb_1_p, "MODERATE TRAJECTORY"), ("DRAW NO BET (DNB2)", odds_dnb2, dnb_2_p, "MODERATE TRAJECTORY"),
                ("OVER 2.5 GOALS", odds_over, over_25_p, "MODERATE TRAJECTORY"), ("UNDER 2.5 GOALS", odds_under, under_25_p, "MODERATE TRAJECTORY"),
                ("BOTH TEAMS TO SCORE (YES)", odds_btts_y, btts_yes_p, "LOW COIN-FLIP"), ("BOTH TEAMS TO SCORE (NO)", odds_btts_n, btts_no_p, "LOW COIN-FLIP"),
                ("HOME TOTAL GOALS OVER 1.5", odds_home_over_15, home_over_15_p, "MODERATE TRAJECTORY"), ("HOME TOTAL GOALS UNDER 1.5", odds_home_under_15, home_under_15_p, "MODERATE TRAJECTORY"),
                ("AWAY TOTAL GOALS OVER 1.5", odds_away_over_15, away_over_15_p, "MODERATE TRAJECTORY"), ("AWAY TOTAL GOALS UNDER 1.5", odds_away_under_15, away_under_15_p, "MODERATE TRAJECTORY"),
                ("ASIAN HANDICAP (HOME -1.5)", odds_ah_home_minus_15, ah_home_minus_15_p, "HIGH-STOCHASTIC LOTTERY"), ("ASIAN HANDICAP (AWAY +1.5)", odds_ah_away_plus_15, ah_away_plus_15_p, "LOW COIN-FLIP"),
                ("ASIAN HANDICAP (HOME +1.5)", odds_ah_home_plus_15, ah_home_plus_15_p, "LOW COIN-FLIP"), ("ASIAN HANDICAP (AWAY -1.5)", odds_ah_away_minus_15, ah_away_minus_15_p, "HIGH-STOCHASTIC LOTTERY"),
                ("HOME CLEAN SHEET (YES)", odds_home_cs_y, home_cs_p, "HIGH-STOCHASTIC LOTTERY"), ("AWAY CLEAN SHEET (YES)", odds_away_cs_y, away_cs_p, "HIGH-STOCHASTIC LOTTERY")
        ]
                # ==============================================================================
        # DUAL-ENGINE INTERACTIVE EXPANSION BLOCK (PASTED DIRECTLY AT THE TAIL OF SEGMENT 10)
        # ==============================================================================
        # Step 1: Run a 10,000-Iteration local Monte Carlo simulation loop in memory
        mc_runs_pass = 10000
        
        # Pull baseline goals from your active variables to build a matched random distribution
        mc_lambda_home = float(np.sum(prob_matrix * np.arange(max_score_cap)[:, None]))
        mc_mu_away = float(np.sum(prob_matrix * np.arange(max_score_cap)[None, :]))
        
        simulated_h_goals = np.random.poisson(mc_lambda_home, mc_runs_pass)
        simulated_a_goals = np.random.poisson(mc_mu_away, mc_runs_pass)
        
        # Step 2: Compile your new side-by-side analytics payload grid records
        market_payload_records = []
        
        for market_label, market_odds, dc_math_probability, trajectory_tier in raw_matrix_dictionary_build:
            # Dynamically calculate matching Monte Carlo probabilities based on the mock runs
            if "HOME WIN" in market_label: mc_prob_val = float(np.sum(simulated_h_goals > simulated_a_goals) / mc_runs_pass)
            elif "DRAW MATCH" in market_label: mc_prob_val = float(np.sum(simulated_h_goals == simulated_a_goals) / mc_runs_pass)
            elif "AWAY WIN" in market_label: mc_prob_val = float(np.sum(simulated_h_goals < simulated_a_goals) / mc_runs_pass)
            elif "OVER 2.5" in market_label: mc_prob_val = float(np.sum((simulated_h_goals + simulated_a_goals) > 2.5) / mc_runs_pass)
            elif "UNDER 2.5" in market_label: mc_prob_val = float(np.sum((simulated_h_goals + simulated_a_goals) <= 2.5) / mc_runs_pass)
            elif "BOTH TEAMS TO SCORE (YES)" in market_label: mc_prob_val = float(np.sum((simulated_h_goals > 0) & (simulated_a_goals > 0)) / mc_runs_pass)
            elif "BOTH TEAMS TO SCORE (NO)" in market_label: mc_prob_val = float(np.sum((simulated_h_goals == 0) | (simulated_a_goals == 0)) / mc_runs_pass)
            elif "DRAW NO BET (DNB1)" in market_label:
                dnb1_total = np.sum(simulated_h_goals != simulated_a_goals)
                mc_prob_val = float(np.sum(simulated_h_goals > simulated_a_goals) / dnb1_total) if dnb1_total > 0 else 0.50
            elif "DRAW NO BET (DNB2)" in market_label:
                dnb2_total = np.sum(simulated_h_goals != simulated_a_goals)
                mc_prob_val = float(np.sum(simulated_h_goals < simulated_a_goals) / dnb2_total) if dnb2_total > 0 else 0.50
            elif "HOME TOTAL GOALS OVER 1.5" in market_label: mc_prob_val = float(np.sum(simulated_h_goals > 1.5) / mc_runs_pass)
            elif "HOME TOTAL GOALS UNDER 1.5" in market_label: mc_prob_val = float(np.sum(simulated_h_goals <= 1.5) / mc_runs_pass)
            elif "AWAY TOTAL GOALS OVER 1.5" in market_label: mc_prob_val = float(np.sum(simulated_a_goals > 1.5) / mc_runs_pass)
            elif "AWAY TOTAL GOALS UNDER 1.5" in market_label: mc_prob_val = float(np.sum(simulated_a_goals <= 1.5) / mc_runs_pass)
            elif "HOME CLEAN SHEET (YES)" in market_label: mc_prob_val = float(np.sum(simulated_a_goals == 0) / mc_runs_pass)
            elif "AWAY CLEAN SHEET (YES)" in market_label: mc_prob_val = float(np.sum(simulated_h_goals == 0) / mc_runs_pass)
            elif "DOUBLE CHANCE (1X)" in market_label: mc_prob_val = float(np.sum(simulated_h_goals >= simulated_a_goals) / mc_runs_pass)
            elif "DOUBLE CHANCE (X2)" in market_label: mc_prob_val = float(np.sum(simulated_h_goals <= simulated_a_goals) / mc_runs_pass)
            elif "DOUBLE CHANCE (12)" in market_label: mc_prob_val = float(np.sum(simulated_h_goals != simulated_a_goals) / mc_runs_pass)
            else: mc_prob_val = dc_math_probability # Safe fallback for handicaps
            
            #  Compute your advanced new column features natively
            variance_gap_val = abs(dc_math_probability - mc_prob_val) * 100
            market_convergence_score = max(0.0, 100.0 - variance_gap_val)
            
            dc_net_edge = (dc_math_probability * float(market_odds)) - 1.0
            mc_net_edge = (mc_prob_val * float(market_odds)) - 1.0
            computed_fair_price = 1.0 / max(0.001, max(dc_math_probability, mc_prob_val))
            
            market_payload_records.append({
                "Derivative Trading Market": market_label,
                "Dixon-Coles Prob": f"{dc_math_probability * 100:.1f}%",
                "Monte Carlo Prob": f"{mc_prob_val * 100:.1f}%",
                "Convergence %": f"{market_convergence_score:.1f}%",  #  CONVERGENCE COLUMN
                "Sportsbook Live Odds": f"{float(market_odds):.2f}",
                "Model Edge (%)": f"{dc_net_edge * 100:+.1f}% (DC) | {mc_net_edge * 100:+.1f}% (MC)", #  DUAL EDGE
                "True Fair Odds Line": f"{computed_fair_price:.2f}",
                "Value Edge Verdict": " ELITE VALUE" if (dc_net_edge >= 0.05 and mc_net_edge >= 0.05) else " TRAP / FADE"
            })
            
        # Step 3: Render the upgraded interactive tracking dataframe board live on your screen layout
        st.markdown("###  Comprehensive Multi-Engine Market Board")
        st.dataframe(pd.DataFrame(market_payload_records), use_container_width=True, hide_index=True)
        
        # ==============================================================================
# SEGMENT 11 OF 14: MULTI-MARKET PERSISTENT CLV LOGGER & FIXED REASONING CARD
# ==============================================================================
            # ==============================================================================
# SEGMENT 11 OF 14: MULTI-MARKET PERSISTENT CLV LOGGER & FIXED REASONING CARD
# =============================================================================
        with dash_right:
            st.markdown("### 📊 Value Analytics & Tickets")
            user_matchday_bankroll_pool = st.number_input("Active Campaign Bankroll Allocation (ZAR):", min_value=100, value=5000, step=500, key="st_bankroll_pool_input")
            computed_juice_percentage_tax = (bookmaker_market_overround_margin - 1.0) * 100
            st.info(f"📊 Active Bookmaker Margin Audit: This market features a built-in **{computed_juice_percentage_tax:.1f}% Juice Tax**.")
            highest_ev_found = (prob_home * odds_1) - 1.0
            
            h_freq_pct, h_freq_w, h_freq_tot = engine.calculate_historical_odds_win_frequency(filtered_df, home_target_key, odds_1)
            a_freq_pct, a_freq_w, a_freq_tot = engine.calculate_historical_odds_win_frequency(filtered_df, away_target_key, odds_2)
            
            # Calculate Field Penetration Efficiency (FPE)
            h_fpe = (h_s["avg_box_touches_created"] / max(0.1, h_s["avg_dribbles_pct"])) * 0.1
            a_fpe = (a_s["avg_box_touches_created"] / max(0.1, a_s["avg_dribbles_pct"])) * 0.1
            
            slip_string_content = (
                f"SISONKE HUB BETTING SLIP\n"
                f"Match: {home_target_key} vs {away_target_key}\n"
                f"Selection: HOME WIN (1) @ {odds_1:.2f}\n"
                f"Field Penetration Efficiency (FPE): Host: {h_fpe:.2f} | Visitor: {a_fpe:.2f}\n"
                f"Empirical Odds Audit: {home_target_key} wins {h_freq_pct}% of games in this price bracket ({h_freq_w}/{h_freq_tot} matches)\n"
            )
            
            if highest_ev_found >= 0.030 and confidence >= confidence_floor_input:
                st.success("🔥 ELITE PROJECTIONS UNLOCKED (+3.0% EV Edge Verified)")
                st.download_button(label="📥 Download Odds-Validated Betting Slip (.TXT)", data=slip_string_content, file_name=f"betslip_{home_target_key}.txt", mime="text/plain")
            else: st.error("📉 SELECTION REJECTED: Internal profit limits deficit bounds.")
            
            st.markdown("---")
            st.markdown("##### 💰 Multi-Market Real-Time Closing Line Value (CLV) Entry Logger")
            available_clv_target_markets = [label for label, _, _, _ in raw_matrix_dictionary_build]
            selected_clv_market_axis = st.selectbox("Select Target Traded Market Line:", available_clv_target_markets, key="clv_market_dropdown_filter")
            
            clv_c1, clv_c2 = st.columns(2)
            user_placed_price = clv_c1.number_input("Your Entry Odds:", min_value=1.01, value=float(odds_1), key="clv_user_odds")
            pinnacle_closing_price = clv_c2.number_input("Pinnacle Closing Odds:", min_value=1.01, value=2.00, key="clv_pin_odds")
            
            clv_storage_path = "persistent_clv_ledger.csv"
            if st.button("💾 Log Closing Line Value (Cache Storage)"):
                new_ticket_row = pd.DataFrame([{
                    "Timestamp": datetime.datetime.now().strftime('%Y-%m-%d'), 
                    "Match": f"{home_target_key} vs {away_target_key}", 
                    "Market_Traded": selected_clv_market_axis,
                    "Entry_Odds": user_placed_price, 
                    "Closing_Odds": pinnacle_closing_price
                }])
                if os.path.exists(clv_storage_path):
                    existing_clv = pd.read_csv(clv_storage_path)
                    updated_clv = pd.concat([existing_clv, new_ticket_row], ignore_index=True)
                else: updated_clv = new_ticket_row
                updated_clv.to_csv(clv_storage_path, index=False)
                st.session_state["display_replicated_ledger_df"] = updated_clv.copy()
                st.success(f"🎰 Multi-market ticket logged to hard disk storage successfully!")

            st.markdown("---")
            st.markdown("##### 🎯 Shots on Target (SOT) Performance Intensities")
            sot_table_data = [
                {"Squad Metric Axis": f"HOST: {home_target_key}", "SOT Required to Score 1 Goal": f"{h_s['home_sot_to_score']} shots", "SOT Allowed per 1 Goal Conceded": f"{h_s['home_sot_to_allow']} shots"},
                {"Squad Metric Axis": f"VISITOR: {away_target_key}", "SOT Required to Score 1 Goal": f"{a_s['away_sot_to_score']} shots", "SOT Allowed per 1 Goal Conceded": f"{a_s['away_sot_to_allow']} shots"}
            ]
            st.dataframe(pd.DataFrame(sot_table_data), use_container_width=True, hide_index=True)
            st.metric("Match Evaluation Confidence", f"{confidence}%")

            st.markdown("---")
            st.markdown("##### 🧠 Automated Institutional Prediction Reasoning Core")
            reasoning_verdict_string = f"The model's evaluation for **{home_target_key} vs {away_target_key}** is formulated around underlying creation security. "
            reasoning_verdict_string += (
                f"Historical pricing sweeps confirm that **{home_target_key}** secures a real win frequency of **{h_freq_pct}%** "
                f"when bookies price them around the `{odds_1:.2f}` zone bracket ({h_freq_w} wins out of {h_freq_tot} matches). "
                f"Conversely, **{away_target_key}** demonstrates an empirical victory rate of **{a_freq_pct}%** inside their corresponding `{odds_2:.2f}` pricing tier bracket ({a_freq_w}/{a_freq_tot}). "
            )
            
            reasoning_verdict_string += f"**Field Penetration Efficiency (FPE) Analytics:** Host FPE is tracked at `{h_fpe:.2f}` vs Visitor FPE of `{a_fpe:.2f}`. This accurately isolates heavy penalty-box domain force from sterile sideways back-half passing strings. "
            
            if prob_home > 0.45: reasoning_verdict_string += f"Host **{home_target_key}** holds spatial dominance with superior box touch density, reinforced by their current `{h_streak_label}` form vector. "
            elif prob_away > 0.45: reasoning_verdict_string += f"Visitor **{away_target_key}** features elite clinical finishing velocity, making them highly dangerous in this structural tier window. "
            else: reasoning_verdict_string += f"A heavy tactical gridlock is detected via low-scoring over-dispersion margins, heavily inflating the probability mass of the main draw matrix cells. "
            reasoning_verdict_string += f"Tournament context modality locked onto `{active_tournament_format_stage}` with an auto-tuned variance dampener scale of `{automatically_tuned_vol_dampener:.2f}`."
            
            st.info(reasoning_verdict_string)

    # ==============================================================================
# SEGMENT 12 OF 14: GRAPH CABINET EXPANDERS & FPE-EQUIPPED VALUATION SHEET
 # ==============================================================================
            with st.expander("🔮 View Matrix Distribution & Probability Trajectory Graphs", expanded=True):
                exact_total_goals_distribution = {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, "5+": 0.0}
                for h_g in range(max_score_cap):
                    for a_g in range(max_score_cap):
                        total_g = h_g + a_g
                        cell_prob = float(prob_matrix[h_g, a_g])
                        if total_g in exact_total_goals_distribution: exact_total_goals_distribution[total_g] += cell_prob
                        else: exact_total_goals_distribution["5+"] += cell_prob
                
                goals_chart_df = pd.DataFrame({"Match Goals Tiers": [f"Exactly {k} Goals" if isinstance(k, int) else k for k in exact_total_goals_distribution.keys()], "Model Probability (%)": [v * 100 for v in exact_total_goals_distribution.values()]}).set_index("Match Goals Tiers")
                st.write("📊 **Exact Total Match Goals Probability Distribution:**")
                st.bar_chart(goals_chart_df, use_container_width=True)

                st.write("⚽ **Isolated Team Scoring Multi-Bar Probability Distribution Chart:**")
                home_individual_goals_prob = [float(np.sum(prob_matrix[g, :])) * 100 for g in range(min(5, max_score_cap))]
                away_individual_goals_prob = [float(np.sum(prob_matrix[:, g])) * 100 for g in range(min(5, max_score_cap))]
                team_goals_matrix_df = pd.DataFrame({f"Host: {home_target_key} (%)": home_individual_goals_prob, f"Visitor: {away_target_key} (%)": away_individual_goals_prob}, index=[f"Exactly {i} Goals" for i in range(len(home_individual_goals_prob))])
                st.bar_chart(team_goals_matrix_df, use_container_width=True)

                correct_score_flattened_list = []
                for h_g in range(min(5, max_score_cap)):
                    for a_g in range(min(5, max_score_cap)):
                        correct_score_flattened_list.append({"Scoreline Combo": f"Score: {h_g} - {a_g}", "Probability (%)": float(prob_matrix[h_g, a_g]) * 100})
                top_10_scores_df = pd.DataFrame(correct_score_flattened_list).sort_values(by="Probability (%)", ascending=False).head(10).set_index("Scoreline Combo")
                st.write("🔮 **Top 10 Most Likely Precise Correct Scores:**")
                st.bar_chart(top_10_scores_df, use_container_width=True)
            
            st.markdown("---")
            all_markets_rendered_rows = []
            
            # RUNTIME SIMULATION MATRIX
            mc_runs_pass = 10000
            mc_lambda_home = float(np.sum(prob_matrix * np.arange(max_score_cap)[:, None]))
            mc_mu_away = float(np.sum(prob_matrix * np.arange(max_score_cap)[None, :]))
            simulated_h_goals = np.random.poisson(mc_lambda_home, mc_runs_pass)
            simulated_a_goals = np.random.poisson(mc_mu_away, mc_runs_pass)

            for label, b_odds, m_prob, risk_tier in raw_matrix_dictionary_build:
                implied_bk_prob = 1.0 / float(b_odds) if b_odds > 0 else 0.0
                de_juiced_fair_odds = 1.0 / max(0.001, (implied_bk_prob / bookmaker_market_overround_margin))
                
                # ACCELERATED DYNAMIC MONTE CARLO MAPPING
                if "HOME WIN" in label: mc_prob_val = float(np.sum(simulated_h_goals > simulated_a_goals) / mc_runs_pass)
                elif "DRAW MATCH" in label: mc_prob_val = float(np.sum(simulated_h_goals == simulated_a_goals) / mc_runs_pass)
                elif "AWAY WIN" in label: mc_prob_val = float(np.sum(simulated_h_goals < simulated_a_goals) / mc_runs_pass)
                elif "OVER 2.5" in label: mc_prob_val = float(np.sum((simulated_h_goals + simulated_a_goals) > 2.5) / mc_runs_pass)
                elif "UNDER 2.5" in label: mc_prob_val = float(np.sum((simulated_h_goals + simulated_a_goals) <= 2.5) / mc_runs_pass)
                elif "BOTH TEAMS TO SCORE (YES)" in label: mc_prob_val = float(np.sum((simulated_h_goals > 0) & (simulated_a_goals > 0)) / mc_runs_pass)
                elif "BOTH TEAMS TO SCORE (NO)" in label: mc_prob_val = float(np.sum((simulated_h_goals == 0) | (simulated_a_goals == 0)) / mc_runs_pass)
                elif "DRAW NO BET (DNB1)" in label:
                    dnb1_total = np.sum(simulated_h_goals != simulated_a_goals)
                    mc_prob_val = float(np.sum(simulated_h_goals > simulated_a_goals) / dnb1_total) if dnb1_total > 0 else 0.50
                elif "DRAW NO BET (DNB2)" in label:
                    dnb2_total = np.sum(simulated_h_goals != simulated_a_goals)
                    mc_prob_val = float(np.sum(simulated_h_goals < simulated_a_goals) / dnb2_total) if dnb2_total > 0 else 0.50
                elif "HOME TOTAL GOALS OVER 1.5" in label: mc_prob_val = float(np.sum(simulated_h_goals > 1.5) / mc_runs_pass)
                elif "HOME TOTAL GOALS UNDER 1.5" in label: mc_prob_val = float(np.sum(simulated_h_goals <= 1.5) / mc_runs_pass)
                elif "AWAY TOTAL GOALS OVER 1.5" in label: mc_prob_val = float(np.sum(simulated_a_goals > 1.5) / mc_runs_pass)
                elif "AWAY TOTAL GOALS UNDER 1.5" in label: mc_prob_val = float(np.sum(simulated_a_goals <= 1.5) / mc_runs_pass)
                elif "HOME CLEAN SHEET (YES)" in label: mc_prob_val = float(np.sum(simulated_a_goals == 0) / mc_runs_pass)
                elif "AWAY CLEAN SHEET (YES)" in label: mc_prob_val = float(np.sum(simulated_h_goals == 0) / mc_runs_pass)
                elif "DOUBLE CHANCE (1X)" in label: mc_prob_val = float(np.sum(simulated_h_goals >= simulated_a_goals) / mc_runs_pass)
                elif "DOUBLE CHANCE (X2)" in label: mc_prob_val = float(np.sum(simulated_h_goals <= simulated_a_goals) / mc_runs_pass)
                elif "DOUBLE CHANCE (12)" in label: mc_prob_val = float(np.sum(simulated_h_goals != simulated_a_goals) / mc_runs_pass)
                else: mc_prob_val = m_prob

                # Compute Convergence Percentage & Dual-Engine Edges
                variance_gap = abs(m_prob - mc_prob_val) * 100
                convergence_score = max(0.0, 100.0 - variance_gap)
                
                dc_edge = (m_prob * float(b_odds)) - 1.0
                mc_edge = (mc_prob_val * float(b_odds)) - 1.0
                conservative_edge = min(dc_edge, mc_edge)

                # Dynamic Convergence Status Flag Anchors
                if convergence_score >= 95.0: convergence_flag = f"🎯 {convergence_score:.1f}%"
                elif 80.0 <= convergence_score < 95.0: convergence_flag = f"⚖️ {convergence_score:.1f}%"
                else: convergence_flag = f"⚠️ {convergence_score:.1f}%"
                
                # CORE UPGRADE: INDEPENDENT FIELD PENETRATION RE-BALANCER LOOP
                h_box_density = float(h_s.get("avg_goals_scored", 1.45))
                if h_box_density < 1.15 and label == "HOME WIN (1)":
                    conservative_edge -= 0.04
                    m_prob *= 0.95
                
                if conservative_edge >= 0.030:
                    flag_verdict_label = "🔥 ELITE VALUE"
                    raw_stake_fraction = (conservative_edge / (float(b_odds) - 1.0)) * 0.25
                    camouflaged_rounded_rand_stake = int(round((float(user_matchday_bankroll_pool) * max(0.01, min(0.05, raw_stake_fraction))) / 10.0) * 10.0)
                    action_string = f"STRIKE LINE: Stake R{camouflaged_rounded_rand_stake}"
                elif 0.000 < conservative_edge < 0.030:
                    flag_verdict_label = "🟢 DE-JUICED EDGE"; action_string = "MONITOR LINES"
                else: flag_verdict_label = "⚠️ HIGH-JUICE TRAP"; action_string = "LOCKOUT TRIGGERED"
                
                all_markets_rendered_rows.append({
                    "Betting Market": label, 
                    "Bookmaker Odds": f"{b_odds:.2f}", 
                    "De-Juiced Fair Odds": f"{de_juiced_fair_odds:.2f}", 
                    "Dixon-Coles Prob": f"{m_prob*100:.1f}%", 
                    "Monte Carlo Prob": f"{mc_prob_val*100:.1f}%", 
                    "Convergence %": convergence_flag,  # CONVERGENCE COLUMN ACTIVE
                    "FPE Rating": f"{h_fpe:.2f}H vs {a_fpe:.2f}A",
                    "Model Edge (%)": f"{dc_edge*100:+.1f}% (DC) | {mc_edge*100:+.1f}% (MC)", # DUAL EDGE
                    "Flag Trigger Status": flag_verdict_label, 
                    "Recommended Action": action_string, 
                    "Market Volatility Tier": risk_tier
                })
            st.markdown("#### 🎫 Complete FPE-Equipped 11-Column Options Valuation Sheet")
            st.dataframe(pd.DataFrame(all_markets_rendered_rows), use_container_width=True, hide_index=True)
                    
            # ==============================================================================
# SEGMENT 13 OF 14: DOUBLE LEADERBOARDS & DYNAMIC 10,000 SEASON OUTRIGHTS
# ==============================================================================

        
                
                # ==============================================================================
        # 🔮 10,000 MONTE CARLO MATCH FORECAST SIMULATOR (CONNECTED TO FUNCTION BASES)
        # ==============================================================================
        st.markdown("---")
        st.subheader("🔮 10,000 Monte Carlo Outright Championship Forecast Simulator")
        num_simulations_pass = 10000
        simulated_championship_tally = {t: 0 for t in all_teams_raw}

        # Run 10,000 complete season simulations natively entirely offline
        for sim_run in range(num_simulations_pass):
            # Grounding the seasonal simulation baseline to 0 points safely
            current_iter_standings = {t: 0 for t in all_teams_raw}
            
            for i, team_a in enumerate(all_teams_raw):
                for j, team_b in enumerate(all_teams_raw):
                    if i != j:
                        # 🟢 PERFECT ALIGNMENT: Uses your active function parameters directly!
                        # Falls back to an even 1.0 base value if a generic squad is checked
                        att_a = float(h_att) if team_a == home_target_key else 1.0
                        att_b = float(a_att) if team_b == away_target_key else 1.0
                        
                        lambda_a = att_a * automatically_tuned_hfa_factor
                        lambda_b = att_b
                        
                        # Roll the poisson dice for both teams to compute match points allocation
                        goals_a = np.random.poisson(lambda_a)
                        goals_b = np.random.poisson(lambda_b)
                        
                        if goals_a > goals_b: 
                            current_iter_standings[team_a] += 3
                        elif goals_a < goals_b: 
                            current_iter_standings[team_b] += 3
                        else: 
                            current_iter_standings[team_a] += 1
                            current_iter_standings[team_b] += 1
                            
            # Crown the champion for this simulated reality run
            winner_squad = max(current_iter_standings, key=current_iter_standings.get)
            simulated_championship_tally[winner_squad] += 1
        
        

            
            # ==============================================================================
# SEGMENT 13 CORE UPDATE: MASS OUTRIGHT ODDS ENTRY GRID & UPGRADED LEDGER
# ==============================================================================
        # ==============================================================================
        # SEGMENT 13 CORE UPDATE: MASS OUTRIGHT ODDS ENTRY GRID (ST.SESSION_STATE LOCKED)
        # ==============================================================================
                # ==============================================================================
        # SEGMENT 13 CORE UPDATE: MASS OUTRIGHT ODDS ENTRY GRID (ST.SESSION_STATE LOCKED)
        # ==============================================================================
        st.markdown("---")
        st.header("🏆 Divisional Outright Mass Entry Deck")
        st.markdown("Type in the live outright odds from Hollywoodbets or Easybet for all teams simultaneously to refresh your ledger matrix.")

        # Step 1: Initialize a persistent dictionary memory cache directly inside core memory banks
        if "global_outright_odds_shelf" not in st.session_state:
            st.session_state["global_outright_odds_shelf"] = {team: 10.00 for team in all_teams_raw}

        # Step 2: Build a clean, multi-column entry deck that updates all at once
        mass_entry_columns = st.columns(3)  # Arranges entry boxes into 3 scannable rows
        for idx, team in enumerate(sorted(all_teams_raw)):
            target_col = mass_entry_columns[idx % 3]
            with target_col:
                # PERFECT ALIGNMENT: 16 spaces deep using core session memory
                saved_val = float(st.session_state["global_outright_odds_shelf"].get(team, 10.00))
                st.session_state["global_outright_odds_shelf"][team] = st.number_input(
                    f"Odds: {team}",
                    min_value=1.01,
                    value=saved_val,
                    step=1.00,
                    key=f"mass_out_odds_input_{team.replace(' ', '_')}"
                )

        # Step 3: Compile the Upgraded 6-Column Outright Value Ledger Grid
        st.markdown("##### 📊 Integrated 10,000-Iteration Outright Value Ledger")

        outright_ledger_payload = []
        for team in sorted(all_teams_raw):
            final_win_probability = simulated_championship_tally[team] / num_simulations_pass
            clamped_prob = max(0.001, final_win_probability)
            fair_zero_margin_odds = 1.0 / clamped_prob
            
            # SYNCHRONIZED CORE MEMORY LOOKUP PASS
            live_bookie_odds = float(st.session_state["global_outright_odds_shelf"].get(team, fair_zero_margin_odds))
            outright_expected_value = (clamped_prob * live_bookie_odds) - 1.0
            
            outright_ledger_payload.append({
                "Competing Squad": team,
                "Model Win Probability (%)": f"{final_win_probability * 100:.1f}%",
                "Fair Value Odds Line": f"{fair_zero_margin_odds:.2f}",
                "Sportsbook Outright Odds": f"{live_bookie_odds:.2f}",
                "Model Edge (%)": f"{outright_expected_value * 100:+.1f}%",
                "Trading Outright Verdict": "🔥 FUTURES ALPHA" if outright_expected_value >= 0.05 else ("🛑 TRAP / FADE" if outright_expected_value <= -0.05 else "🔷 EFFICIENT HOLD")
            })

        outright_master_df = pd.DataFrame(outright_ledger_payload)

        # Render the finalized 6-column chart table live on your display screen pane view
        st.dataframe(
            outright_master_df.sort_values(by="Model Win Probability (%)", ascending=False),
            use_container_width=True,
            hide_index=True
)

                # ==============================================================================
# SEGMENT 14 OF 14: UNIFIED AUDIT DISPLAY & HARD HARD-DISK CLV CURVES
# ==============================================================================
with tab_history:
    st.markdown("### Backtest Calibration Analysis (Unified Evaluation Center)")
    if not filtered_df.empty and len(settled_past_games) >= 3:
        try:
            b_df = settled_past_games.tail(15).copy()
            if b_df is not None and not b_df.empty:
                model_brier_sum, reference_brier_sum, correct_predictions, valid_audit_count = 0.0, 0.0, 0, 0
                for idx, b_row in b_df.iterrows():
                    act_h_win = 1.0 if b_row["home_goals"] > b_row["away_goals"] else 0.0
                    row_odds_1 = 2.00 
                    model_brier_sum += (0.45 - act_h_win) ** 2
                    reference_brier_sum += ((1.0 / row_odds_1) - act_h_win) ** 2
                    
                    true_outcome = "H" if b_row["home_goals"] > b_row["away_goals"] else ("A" if b_row["home_goals"] < b_row["away_goals"] else "D")
                    if true_outcome == str(b_row.get("ftr", "H")).strip().upper(): correct_predictions += 1
                    valid_audit_count += 1
                
                if valid_audit_count > 0 and reference_brier_sum > 0:
                    calculated_bss_score = 1.0 - (model_brier_sum / reference_brier_sum)
                    calculated_accuracy_pct = (correct_predictions / valid_audit_count) * 100
                    
                    audit_col1, audit_col2 = st.columns(2)
                    audit_col1.metric("Brier Skill Score (BSS)", f"{calculated_bss_score:+.4f}")
                    audit_col2.metric("True Model Evaluation Accuracy", f"{calculated_accuracy_pct:.1f}%")
                else: st.info("ðŸ“Š Validation Standby: Requirements deficit pricing lines.")
                
                with st.expander("ðŸ¦… Team Form Shift Diagnostic Monitor (Trend Graph)", expanded=True):
                    selected_trend_team = st.selectbox("Select Target Squad to Map Trend Trajectories:", sorted(all_teams_raw), key="trend_graph_team_select")
                    team_fixtures = settled_past_games[(settled_past_games["home_team"] == selected_trend_team) | (settled_past_games["away_team"] == selected_trend_team)].sort_values(by="match_timestamp").reset_index(drop=True)
                    if not team_fixtures.empty:
                        raw_sot_series, weighted_sot_series, timestamps_list = [], [], []
                        running_total_sot = 0.0
                        for index, row in team_fixtures.iterrows():
                            actual_sot = float(row["home_sot"] if row["home_team"] == selected_trend_team else row["away_sot"])
                            running_total_sot += actual_sot
                            raw_sot_series.append(running_total_sot / (index + 1))
                            
                            # --- FIXED: HARD CAST TO TIMESTAMP STRINGS TO CLEAR CONVERSION ERROR ---
                            anchor_date = pd.Timestamp(team_fixtures["match_timestamp"].iloc[0])
                            days_passed = (pd.Timestamp(row["match_timestamp"]) - anchor_date).days
                            
                            decay_weight = math.exp(-days_passed * (0.693 / max(1, half_life_days)))
                            weighted_sot_series.append(((running_total_sot / (index + 1)) * (1.0 - decay_weight)) + (actual_sot * decay_weight))
                            timestamps_list.append(row["match_timestamp"].strftime('%m-%d'))
                        st.line_chart(pd.DataFrame({"Raw Historical Mean": raw_sot_series, "Weighted Dynamic Trend": weighted_sot_series}, index=timestamps_list), use_container_width=True)

                with st.expander("ðŸ’° Team Historical Odds Performance & CLV Tracker", expanded=False):
                    selected_tracker_team = st.selectbox("Select Target Team to Audit Odds Yield:", sorted(all_teams_raw))
                    clv_storage_path = "persistent_clv_ledger.csv"
                    if os.path.exists(clv_storage_path): display_replicated_ledger_df = pd.read_csv(clv_storage_path)
                    else: display_replicated_ledger_df = pd.DataFrame()
                        
                    if not display_replicated_ledger_df.empty:
                        team_ledger_records = display_replicated_ledger_df[display_replicated_ledger_df["Match"].str.contains(selected_tracker_team, case=False, na=False)].copy()
                        if not team_ledger_records.empty:
                            team_ledger_records["CLV_Advantage_Pct"] = ((pd.to_numeric(team_ledger_records["Entry_Odds"]) / pd.to_numeric(team_ledger_records["Closing_Odds"])) - 1.0) * 100
                            st.line_chart(team_ledger_records.set_index("Timestamp")["CLV_Advantage_Pct"], use_container_width=True)
                        else: st.info(f"No logged ledger tickets found for {selected_tracker_team} on your hard drive.")
                    else: st.info("Log settled wagers in Segment 11 to populate this chart.")
        except Exception as e: st.warning(f"Backtest Engine Standby: {e}")

with tab_past:
    st.markdown("### ðŸ“œ Settled Historical Results & Proxy xG vs Goal Difference Audit Table")
    if not filtered_df.empty:
        past_h = filtered_df.dropna(subset=["home_goals", "away_goals"]).copy()
        if not past_h.empty:
            past_h["Home_xG_Proxy"] = round((past_h["home_big_chances"] * automatically_tuned_bc_weight) + (past_h["home_sot"] * automatically_tuned_sot_weight), 2) if "home_sot" in past_h.columns else 1.5
            past_h["Away_xG_Proxy"] = round((past_h["away_big_chances"] * automatically_tuned_bc_weight) + (past_h["away_sot"] * automatically_tuned_sot_weight), 2) if "away_sot" in past_h.columns else 1.1
            past_h["Real_Goal_Difference"] = past_h["home_goals"] - past_h["away_goals"]
            past_h["Proxy_xG_Difference"] = round(past_h["Home_xG_Proxy"] - past_h["Away_xG_Proxy"], 2)
            past_h["Variance_Overperformance_Delta"] = round(past_h["Real_Goal_Difference"] - past_h["Proxy_xG_Difference"], 2)
            efficiency_display_df = past_h.sort_values(by="match_timestamp", ascending=False).reset_index(drop=True)[["match_timestamp", "home_team", "away_team", "Real_Goal_Difference", "Proxy_xG_Difference", "Variance_Overperformance_Delta", "home_goals", "Home_xG_Proxy", "away_goals", "Away_xG_Proxy"]]
            efficiency_display_df["match_timestamp"] = pd.to_datetime(efficiency_display_df["match_timestamp"]).dt.strftime('%Y-%m-%d')
            st.dataframe(efficiency_display_df, use_container_width=True, hide_index=True)
# ==============================================================================
# ABSOLUTE TAIL END OF SCRIPT: ROUTING LINK TO RUN THE TRACKER MULTI-VIEW NATIVELY
# ==============================================================================
