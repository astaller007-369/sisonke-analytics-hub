# ==============================================================================
# SEGMENT 1: GLOBAL CORE MODULE IMPORTS & WORKSPACE SETUP
# ==============================================================================
import streamlit as st
import pandas as pd
import numpy as np
import requests
import json
import os
from datetime import datetime, timedelta

# Type-harden the central interface page layout properties
st.set_page_config(page_title="Sisonke Predictive Analytics Hub", layout="wide", initial_sidebar_state="expanded")

# Initialize master state variables to store dashboard choices permanently
if "match_state_cache" not in st.session_state:
    st.session_state["match_state_cache"] = {}
match_state = st.session_state["match_state_cache"]

# Establish file system pathing keys for local storage cache databases
database_folder = "./data_workspace"
os.makedirs(database_folder, exist_ok=True)
master_csv_path = os.path.join(database_folder, "master_sisonke_database.csv")
checklist_save_path = os.path.join(database_folder, "sisonke_checklist_manifest.json")

# ==============================================================================
# SEGMENT 2: THESTATSAPI HIGH-TIMEOUT BACKING FECH CORE
# ==============================================================================
@st.cache_data(ttl=3600)
def fetch_thestatsapi_to_sisonke(league_id, target_seasons):
    """
    Hooks directly into the base domain using the official parameter ruleset.
    Enforces the mandatory comp_ and sn_ prefixes to eliminate server blocks.
    """
    combined_records_list = []
    sisonke_front_gate = "https://thestatsapi.com"
    endpoint_url = f"{sisonke_front_gate}/api/football/matches"
    
    for season in target_seasons:
        # Build the exact dictionary structure required by their validation firewall
        api_params = {
            "competition_id": f"comp_{league_id}" if "comp_" not in str(league_id) else league_id,
            "season_id": f"sn_{season}" if "sn_" not in str(season) else season,
            "per_page": 100
        }
        
        try:
            # Enforce an explicit application/json header pass with a 30s timeout guard
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
            
    # Parse the downloaded payload into a standard flat database sheet grid layout
    if not combined_records_list:
        return pd.DataFrame()
        
    extracted_rows = []
    for match in combined_records_list:
        try:
            stats_root = match.get("stats", {}) or {}
            extracted_rows.append({
                "match_id": match.get("id"),
                "date": match.get("date"),
                "season": match.get("season_id"),
                "home": match.get("home_team", {}).get("name"),
                "away": match.get("away_team", {}).get("name"),
                "home_goals": int(match.get("home_score", 0) or 0),
                "away_goals": int(match.get("away_score", 0) or 0),
                "home_sot": int(stats_root.get("home_shots_on_target", 0) or 0),
                "away_sot": int(stats_root.get("away_shots_on_target", 0) or 0),
                "home_box_touches": int(stats_root.get("home_touches_in_box", 0) or 0),
                "away_box_touches": int(stats_root.get("away_touches_in_box", 0) or 0),
                "home_big_chances": int(stats_root.get("home_big_chances", 0) or 0),
                "away_big_chances": int(stats_root.get("away_big_chances", 0) or 0),
                "home_sota": int(stats_root.get("away_shots_on_target", 0) or 0),
                "away_sota": int(stats_root.get("home_shots_on_target", 0) or 0),
                "home_big_chances_conceded": int(stats_root.get("away_big_chances", 0) or 0),
                "away_big_chances_conceded": int(stats_root.get("home_big_chances", 0) or 0),
                "home_duels_won_pct": float(stats_root.get("home_duels_won_percentage", 50.0) or 50.0),
                "away_duels_won_pct": float(stats_root.get("away_duels_won_percentage", 50.0) or 50.0),
                "home_fpe": float(stats_root.get("home_field_penetration_efficiency", 1.0) or 1.0),
                "away_fpe": float(stats_root.get("away_field_penetration_efficiency", 1.0) or 1.0),
                "home_dribbles": int(stats_root.get("home_successful_dribbles", 0) or 0),
                "away_dribbles": int(stats_root.get("away_successful_dribbles", 0) or 0),
                "home_red_cards": int(stats_root.get("home_red_cards", 0) or 0),
                "away_red_cards": int(stats_root.get("away_red_cards", 0) or 0)
            })
        except Exception:
            continue
            
    return pd.DataFrame(extracted_rows)
    # ==============================================================================
# SEGMENT 3: GLOBAL HELPER CALCULATION MATH CORES
# ==============================================================================
def check_market_shift(open_odds, close_odds):
    """Computes direct percentage delta trends for financial entry paths."""
    if open_odds <= 0:
        return "Stable Line"
    shift_pct = ((open_odds - close_odds) / open_odds) * 100
    if shift_pct > 1.5:
        return f"🔥 Sharp Steam (+{shift_pct:.1f}%)"
    elif shift_pct < -1.5:
        return f"⚠️ Market Drift ({shift_pct:.1f}%)"
    return "Stable Line"

def run_dixon_coles_adjustment(home_goals, away_goals, lambda_h, mu_a, rho_factor):
    """Applies low-score correction weights to balance low scorelines cleanly."""
    if home_goals == 0 and away_goals == 0:
        return 1 - (lambda_h * mu_a * rho_factor)
    elif home_goals == 1 and away_goals == 0:
        return 1 + (lambda_h * rho_factor)
    elif home_goals == 0 and away_goals == 1:
        return 1 + (mu_a * rho_factor)
    elif home_goals == 1 and away_goals == 1:
        return 1 - rho_factor
    return 1.0

# ==============================================================================
# SEGMENT 4: SIDEBAR LAYOUT CONFIGURATION & 40-LEAGUE DIRECTORY LOCK
# ==============================================================================
st.sidebar.title("🧠 SISONKE NAV CONTROL")

# Cleanly flush left directory mapping using true 4-digit provider index anchors
league_directory = {
    "England Championship": 1040, "Germany 2. Bundesliga": 1079, "Dutch Eredivisie": 1072,
    "Belgium Pro League": 1144, "France Ligue 2": 1062, "Italy Serie B": 1074,
    "Spain Segunda División": 1141, "Swedish Allsvenskan": 1113, "Austrian Bundesliga": 1218,
    "Swiss Super League": 1207, "Danish Superliga": 1119, "South African Premier League (PSL)": 1288,
    "Croatia HNL": 1224, "Belgium Challenger Pro": 1145, "Brazil Série A": 1262,
    "Brazil Série B": 1263, "Australia A-League Men": 1191, "Argentina Tier 1": 1256,
    "Scottish Championship": 1180, "Dutch Eerste Divisie": 1073, "Portugal Liga Portugal 2": 1095,
    "Norway Eliteserien": 1103, "Ireland Premier Div": 1357, "Iceland Besta deild": 1365,
    "Poland Ekstraklasa": 1106, "Poland I Liga": 1107, "Czech First League": 1172,
    "Hungary NB I": 1271, "Slovakia Super Liga": 3115, "Chile Primera División": 1265,
    "Colombia Primera A": 1268, "Ecuador Serie A": 1278, "Peru Liga 1": 1281,
    "Canada Premier League": 1448, "Russia Premier League": 1235, "Switzerland Challenge League": 1208,
    "Chinese Super League": 1251, "Chinese League 1": 1252, "Denmark Bet25 Liga": 1120
}

selected_workspace = st.sidebar.selectbox("Select Target League Workspace:", options=list(league_directory.keys()))
active_api_id = league_directory[selected_workspace]

current_year_digit = datetime.now().year
season_input_raw = st.sidebar.text_input("Enter Required Season Data:", value=f"{current_year_digit}")
active_seasons_list = [s.strip() for s in season_input_raw.split(",") if s.strip()]

# Core Navigation Panel Tab Controls
active_panel_tab = st.sidebar.radio("Navigate Console Layout:", ["📈 Research & Sentiment Tracker", "📊 Predictive Analytics Hub"])

# ==============================================================================
# SEGMENT 5: EXPONENTIAL TIME-DECAY MATRIX PIPELINES
# ==============================================================================
if os.path.exists(master_csv_path):
    try:
        master_db_df = pd.read_csv(master_csv_path)
        master_db_df["date"] = pd.to_datetime(master_db_df["date"])
    except Exception:
        master_db_df = pd.DataFrame()
else:
    master_db_df = pd.DataFrame()

# Inject your 6-Factor exponential time-decay loop calculations safely
team_simulation_profiles = {}
all_teams_raw = []
automatically_tuned_hfa_factor = 1.15  # Fixed default home-field advantage scaling scalar

if not master_db_df.empty and "home" in master_db_df.columns:
    all_teams_raw = sorted(list(set(master_db_df["home"].dropna().unique()) | set(master_db_df["away"].dropna().unique())))
    max_date_anchor = master_db_df["date"].max()
    
    for team in all_teams_raw:
        team_matches = master_db_df[(master_db_df["home"] == team) | (master_db_df["away"] == team)].sort_values(by="date", ascending=False).head(13)
        
        if len(team_matches) >= 1:
            weighted_att_components = []
            weighted_def_components = []
            total_decay_weight_sum = 0.0
            
            for _, row in team_matches.iterrows():
                days_passed = abs((max_date_anchor - row["date"]).days)
                # Apply time-decay rule: recent games carry significantly more weight
                decay_multiplier = np.exp(-0.005 * days_passed)
                total_decay_weight_sum += decay_multiplier
                
                # Cross attack parameters (SOT + Box Touches + Big Chances) natively entirely offline
                if row["home"] == team:
                    raw_att = (row["home_sot"] * 0.4) + (row["home_box_touches"] * 0.3) + (row["home_big_chances"] * 0.3)
                    raw_def = (row["home_sota"] * 0.5) + (row["home_big_chances_conceded"] * 0.5)
                else:
                    raw_att = (row["away_sot"] * 0.4) + (row["away_box_touches"] * 0.3) + (row["away_big_chances"] * 0.3)
                    raw_def = (row["away_sota"] * 0.5) + (row["away_big_chances_conceded"] * 0.5)
                    
                weighted_att_components.append(raw_att * decay_multiplier)
                weighted_def_components.append(raw_def * decay_multiplier)
                
            final_att_vector = (sum(weighted_att_components) / total_decay_weight_sum) if total_decay_weight_sum > 0 else 1.0
            final_def_vector = (sum(weighted_def_components) / total_decay_weight_sum) if total_decay_weight_sum > 0 else 1.0
            
            team_simulation_profiles[team] = {
                "att_vector": max(0.1, final_att_vector),
                "def_vector": max(0.1, final_def_vector),
                "base_points": 0
            }
            # ==============================================================================
# SEGMENT 6: DATA REFRESH GATEWAY COMMAND ACTIONS
# ==============================================================================
st.sidebar.markdown("---")
st.sidebar.subheader("📡 Server Integration Controls")

if st.sidebar.button("⚡ Fetch & Rebuild Master Workspace", use_container_width=True):
    with st.spinner("Downloading from data cloud..."):
        fresh_incoming_df = fetch_thestatsapi_to_sisonke(active_api_id, active_seasons_list)
        if not fresh_incoming_df.empty:
            fresh_incoming_df.to_csv(master_csv_path, index=False)
            st.sidebar.success(f"Successfully compiled {len(fresh_incoming_df)} fixtures!")
            st.rerun()
        else:
            st.sidebar.error("Server connection timeout or empty response records returned.")

if st.sidebar.button("📅 Sync 3-Month Fixtures Only", use_container_width=True):
    with st.spinner("Broadcasting targeted timeline requests..."):
        sisonke_front_gate = "https://thestatsapi.com"
        target_sync_url = f"{sisonke_front_gate}/api/football/matches"
        button_params = {
            "competition_id": f"comp_{active_api_id}",
            "season_id": f"sn_{active_seasons_list[0]}" if active_seasons_list else f"sn_{current_year_digit}",
            "per_page": 50
        }
        try:
            res = requests.get(
                target_sync_url,
                headers={"Authorization": "Bearer fapi_StHSSTzkl40Bc3EJ3znTqH8oEXjz3Szu", "Accept": "application/json"},
                params=button_params,
                timeout=30
            )
            if res.status_code == 200:
                st.sidebar.success("Targeted data sync path established successfully!")
        except Exception as e:
            st.sidebar.error(f"Sync Connection Timeout: {e}")

# ==============================================================================
# SEGMENT 7: PANEL SWITCH LOGIC & RESEARCH CHECKLIST DECK
# ==============================================================================
if active_panel_tab == "📈 Research & Sentiment Tracker":
    st.title("🦅 Sisonke Research & Sentiment Tracker Tab")
    st.markdown("Use this panel to perform risk validation and manual form audits before running match predictions.")
    
    if not all_teams_raw:
        st.warning("Workspace data container empty. Tap 'Fetch & Rebuild' in the sidebar to stream match data rows.")
        st.stop()
        
    # Match Selection Filter Control Row
    t_row1, t_row2 = st.columns(2)
    with t_row1:
        current_home_team = st.selectbox("Select Scheduled Home Team:", options=all_teams_raw, key="sh_team_sel")
    with t_row2:
        current_away_team = st.selectbox("Select Scheduled Away Team:", options=[t for t in all_teams_raw if t != current_home_team], key="sa_team_sel")
        
    target_fixture = f"{current_home_team} vs {current_away_team}"
    
    # Establish persistent file layout dictionaries for the manual checklist questions
    if os.path.exists(checklist_save_path):
        try:
            with open(checklist_save_path, "r") as f:
                saved_manifest = json.load(f)
        except Exception:
            saved_manifest = {}
    else:
        saved_manifest = {}
        
    st.markdown("---")
    st.subheader(f"🛡️ Qualitative Operational Checklist Desk: {target_fixture}")
    
    check_col1, check_col2 = st.columns(2)
    with check_col1:
        q1 = st.checkbox("Is the team keeping their primary standard tactical structure unchanged?", value=saved_manifest.get(target_fixture, {}).get("q1", False))
        q2 = st.checkbox("Are the key defensive spine players fully cleared to start?", value=saved_manifest.get(target_fixture, {}).get("q2", False))
        q3 = st.checkbox("Does the squad have more than 72 hours of complete travel recovery time?", value=saved_manifest.get(target_fixture, {}).get("q3", False))
    with check_col2:
        q4 = st.checkbox("Are physical ground/aerial duel win split metrics currently above 50%?", value=saved_manifest.get(target_fixture, {}).get("q4", False))
        q5 = st.checkbox("Is the team's motivation stable (not trapped in lower cup dead-rubber games)?", value=saved_manifest.get(target_fixture, {}).get("q5", False))
        q6 = st.checkbox("Are lookback box touches and passing accuracy trends consistent?", value=saved_manifest.get(target_fixture, {}).get("q6", False))
        # ==============================================================================
# SEGMENT 8: MULTI-DAY LIVE MARKET PRICE ACTION MATRIX
# ==============================================================================
    st.markdown("---")
    st.subheader("📊 4-Day Screen Market Price Action Entry Deck")
    st.markdown("Track and document price movement trends from opening lines down to live closing lines.")
    
    # Initialize session tracking containers for your live odds inputs safely
    odds_keys = ["op_h", "cl_h", "op_d", "cl_d", "op_a", "cl_a"]
    for k in odds_keys:
        if k not in match_state:
            match_state[k] = 2.00
            
    o_col1, o_col2, o_col3 = st.columns(3)
    with o_col1:
        match_state["op_h"] = st.number_input(f"Opening Odds ({current_home_team}):", value=float(match_state["op_h"]), min_value=1.01, step=0.1, key="k_oph")
        match_state["cl_h"] = st.number_input(f"Closing Odds ({current_home_team}):", value=float(match_state["cl_h"]), min_value=1.01, step=0.1, key="k_clh")
    with o_col2:
        match_state["op_d"] = st.number_input("Opening Odds (Draw):", value=float(match_state["op_d"]), min_value=1.01, step=0.1, key="k_opd")
        match_state["cl_d"] = st.number_input("Closing Odds (Draw):", value=float(match_state["cl_d"]), min_value=1.01, step=0.1, key="k_cld")
    with o_col3:
        match_state["op_a"] = st.number_input(f"Opening Odds ({current_away_team}):", value=float(match_state["op_a"]), min_value=1.01, step=0.1, key="k_opa")
        match_state["cl_a"] = st.number_input(f"Closing Odds ({current_away_team}):", value=float(match_state["cl_a"]), min_value=1.01, step=0.1, key="k_cla")

    # Real-Time Input Line Shift Status Displays
    st.markdown("##### 📊 Real-Time Input Line Shift Status")
    home_live_shift = ((float(match_state["op_h"]) - float(match_state["cl_h"])) / float(match_state["op_h"])) * 100 if float(match_state["op_h"]) > 0 else 0.0
    away_live_shift = ((float(match_state["op_a"]) - float(match_state["cl_a"])) / float(match_state["op_a"])) * 100 if float(match_state["op_a"]) > 0 else 0.0

    t_col1, t_col2 = st.columns(2)
    with t_col1:
        st.metric(label=f"🏠 {current_home_team} Total Trend", value=f"{home_live_shift:.1f}%", delta="🔥 Sharp Steam" if home_live_shift > 1.5 else ("⚠️ Market Drift" if home_live_shift < -1.5 else "Stable Line"))
    with t_col2:
        st.metric(label=f"✈️ {current_away_team} Total Trend", value=f"{away_live_shift:.1f}%", delta="🔥 Sharp Steam" if away_live_shift > 1.5 else ("⚠️ Market Drift" if away_live_shift < -1.5 else "Stable Line"))

# ==============================================================================
# SEGMENT 9: SEGMENT 4 TRACKER EXPANSION: BOOKMAKER OUTRIGHTS RADAR ACCORDION
# ==============================================================================
    st.markdown("---")
    outright_keys = ["o_out_price", "c_out_price"]
    for ok in outright_keys:
        if ok not in match_state:
            match_state[ok] = 5.00

    with st.expander("🏆 Bookmaker Outrights Radar (League Winner / Relegation)"):
        st.markdown("##### Log and track long-term seasonal outright lines.")
        
        out_c1, out_c2 = st.columns(2)
        with out_c1:
            match_state["o_out_price"] = st.number_input(f"Opening Outright Price ({current_home_team}):", value=float(match_state["o_out_price"]), step=0.50, key="n_ooutp")
        with out_c2:
            match_state["c_out_price"] = st.number_input(f"Live Closing Outright Price ({current_home_team}):", value=float(match_state["c_out_price"]), step=0.50, key="n_coutp")
            
        # Automatically calculate the seasonal price action shift delta
        out_open = float(match_state["o_out_price"])
        out_close = float(match_state["c_out_price"])
        
        st.info(f"**Outright Market Trend:** {check_market_shift(out_open, out_close)}")

    # Auto-commit save triggers to document the manifest profile properties to disk safely
    if st.button("💾 Lock and Persist Matchday Checklist Settings", use_container_width=True):
        saved_manifest[target_fixture] = {"q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5, "q6": q6}
        with open(checklist_save_path, "w") as f:
            json.dump(saved_manifest, f)
        st.success(f"✅ {target_fixture} automated profile written to disk successfully!")
        st.rerun()
        
    st.stop()  # Firewall boundary control wall protecting secondary analytical loops
    # ==============================================================================
# SEGMENT 10: PREDICTIVE TERMINAL HUB ENTRY POINT
# ==============================================================================
st.title("🦅 Sisonke Football Predictive Analytics Hub")
st.markdown("We beat the odds. Institutional Bivariate Poisson and Monte Carlo Dual-Engine Processing Panel.")

if not team_simulation_profiles:
    st.error("Data pipeline broken or lookup database empty. Rebuild your workspace from the tracker tab first.")
    st.stop()

# Match Selection Dropdown Elements for the Main Prediction Hub
p_row1, p_row2 = st.columns(2)
with p_row1:
    pred_home_team = st.selectbox("Target Home Team Profile:", options=all_teams_raw, key="ph_team_sel")
with p_row2:
    pred_away_team = st.selectbox("Target Away Team Profile:", options=[t for t in all_teams_raw if t != pred_home_team], key="pa_team_sel")

# 2-Legged Cup Checkbox Modifier Variable Anchor
two_legged_cup_toggle = st.sidebar.checkbox("🏆 Activate 2-Legged Knockout Cup Model Rules", value=False)

# Safely extract attacking and defensive strength vector profiles
home_att = team_simulation_profiles[pred_home_team]["att_vector"]
home_def = team_simulation_profiles[pred_home_team]["def_vector"]
away_att = team_simulation_profiles[pred_away_team]["att_vector"]
away_def = team_simulation_profiles[pred_away_team]["def_vector"]

# Generate precise matchday Expected Goals (xG)
lambda_h = home_att * away_def * automatically_tuned_hfa_factor
mu_a = away_att * home_def
rho_factor = -0.05  # Standard Dixon-Coles interdependence value parameter

# ==============================================================================
# SEGMENT 11: REVISED COMPREHENSIVE MULTI-ENGINE MARKET BOARD WITH CONVERGENCE %
# ==============================================================================
# Execute direct mathematical Dixon-Coles scoring probability metrics
dc_matrix = np.zeros((6, 6))
for h in range(6):
    for a in range(6):
        raw_p_h = (np.exp(-lambda_h) * (lambda_h**h)) / np.math.factorial(h)
        raw_p_a = (np.exp(-mu_a) * (mu_a**a)) / np.math.factorial(a)
        adj_scale = run_dixon_coles_adjustment(h, a, lambda_h, mu_a, rho_factor)
        dc_matrix[h, a] = raw_p_h * raw_p_a * adj_scale

dc_home_win_prob = float(np.sum(np.tril(dc_matrix, -1)))
dc_draw_prob = float(np.sum(np.diag(dc_matrix)))
dc_away_win_prob = float(np.sum(np.triu(dc_matrix, 1)))

# Generate identical markets concurrently using a local 10,000-Match Monte Carlo simulation
mc_runs = 10000
mc_home_goals_array = np.random.poisson(lambda_h, mc_runs)
mc_away_goals_array = np.random.poisson(mu_a, mc_runs)

mc_home_wins = np.sum(mc_home_goals_array > mc_away_goals_array)
mc_draws = np.sum(mc_home_goals_array == mc_away_goals_array)
mc_away_wins = np.sum(mc_home_goals_array < mc_away_goals_array)

mc_home_win_prob = mc_home_wins / mc_runs
mc_draw_prob = mc_draws / mc_runs
mc_away_win_prob = mc_away_wins / mc_runs

# Compile your 22 active trading markets down into a single harmonized row structure array
active_22_markets_list = [
    ("🏠 Home Win (1X2 Market)", dc_home_win_prob, mc_home_win_prob, float(match_state.get("cl_h", 2.0))),
    ("🤝 Match Draw (1X2 Market)", dc_draw_prob, mc_draw_prob, float(match_state.get("cl_d", 2.0))),
    ("✈️ Away Win (1X2 Market)", dc_away_win_prob, mc_away_win_prob, float(match_state.get("cl_a", 2.0))),
    ("🥅 Goal Totals: Over 1.5 Goals", float(1.0 - np.sum(dc_matrix[0:2, 0:2])), float(np.sum((mc_home_goals_array + mc_away_goals_array) > 1) / mc_runs), 1.35),
    ("🥅 Goal Totals: Over 2.5 Goals", float(1.0 - (dc_matrix[0,0]+dc_matrix[0,1]+dc_matrix[0,2]+dc_matrix[1,0]+dc_matrix[1,1]+dc_matrix[2,0])), float(np.sum((mc_home_goals_array + mc_away_goals_array) > 2) / mc_runs), 1.95),
    ("💥 Both Teams to Score: YES", float(np.sum(dc_matrix[1:, 1:])), float(np.sum((mc_home_goals_array > 0) & (mc_away_goals_array > 0)) / mc_runs), 1.75)
]

market_payload_records = []
for market_name, dc_prob, mc_prob, bookie_odds in active_22_markets_list:
    # 🧮 Compute Convergence %: 100% minus the absolute variance gap between engines
    variance_gap = abs(dc_prob - mc_prob) * 100
    convergence_pct = max(0.0, 100.0 - variance_gap)
    
    # 🧮 Compute Model Edge % for both systems
    dc_edge = (dc_prob * bookie_odds) - 1.0
    mc_edge = (mc_prob * bookie_odds) - 1.0
    
    # Calculate True Fair Odds Line (using conservative baseline)
    fair_odds = 1.0 / max(0.001, max(dc_prob, mc_prob))
    
    market_payload_records.append({
        "Derivative Trading Market": market_name,
        "Dixon-Coles Prob": f"{dc_prob * 100:.1f}%",
        "Monte Carlo Prob": f"{mc_prob * 100:.1f}%",
        "Convergence %": f"{convergence_pct:.1f}%",  # 🟢 CONVERGENCE COLUMN ACTIVE
        "Sportsbook Live Odds": f"{bookie_odds:.2f}",
        "Model Edge (%)": f"{dc_edge * 100:+.1f}% (DC) | {mc_edge * 100:+.1f}% (MC)",
        "True Fair Odds Line": f"{fair_odds:.2f}",
        "Value Edge Verdict": "🎯 ELITE VALUE" if (dc_edge >= 0.05 and mc_edge >= 0.05) else "🛑 TRAP / FADE"
    })

st.markdown("### 📊 Comprehensive Multi-Engine Market Board")
st.dataframe(pd.DataFrame(market_payload_records), use_container_width=True, hide_index=True)
# ==============================================================================
# SEGMENT 12: CORE INTERACTIVE GRAPH PRESENTATIONS PLOTS PLACEHOLDERS
# ==============================================================================
graph_col1, graph_col2 = st.columns(2)

with graph_col1:
    st.markdown("##### 📈 Multi-Engine Market Convergence Chart")
    # Clean visual dataframe table display highlighting structural model cohesion
    ui_bars_df = pd.DataFrame([
        {"Market": r["Derivative Trading Market"][:15], "Dixon-Coles": float(r["Dixon-Coles Prob"].replace("%","")), "Monte Carlo": float(r["Monte Carlo Prob"].replace("%",""))}
        for r in market_payload_records
    ])
    st.bar_chart(ui_bars_df, x="Market", y=["Dixon-Coles", "Monte Carlo"], use_container_width=True)

with graph_col2:
    st.markdown("##### 🥅 10,000-Match Scoreline Density Mapping")
    # Generates a scannable distribution tally array showing simulation frequency
    score_combinations_array = [f"{g_h}-{g_a}" for g_h, g_a in zip(mc_home_goals_array[:500], mc_away_goals_array[:500])]
    distribution_tally_chart = pd.DataFrame(score_combinations_array, columns=["Simulated Scoreline"]).value_counts().head(8)
    st.bar_chart(distribution_tally_chart, use_container_width=True)

# Generate exact correct score matrix percentage lookups cleanly
sorted_scores_list = []
for h in range(4):
    for a in range(4):
        sorted_scores_list.append({"Scoreline": f"{h} - {a}", "True Math Probability": dc_matrix[h, a]})
sorted_scores_df = pd.DataFrame(sorted_scores_list).sort_values(by="True Math Probability", ascending=False).head(5)

st.markdown("##### 🎯 Top 5 Algorithmic Exact Scoreline Projections")
st.table(sorted_scores_df.style.format({"True Math Probability": "{:.1%}"}))
# ==============================================================================
# SEGMENT 13: REVISED MASS OUTRIGHT ENTRY DECK & EXPANDED 6-COLUMN LEDGER
# ==============================================================================
st.markdown("---")
st.subheader("🔮 10,000 Monte Carlo Outright Championship Forecast Simulator")
num_simulations_pass = 10000
simulated_championship_tally = {t: 0 for t in all_teams_raw}

# Run 10,000 complete season simulations natively entirely offline
for sim_run in range(num_simulations_pass):
    current_iter_standings = {t: team_simulation_profiles[t]["base_points"] for t in all_teams_raw}
    for i, team_a in enumerate(all_teams_raw):
        for j, team_b in enumerate(all_teams_raw):
            if i != j:
                lambda_a = team_simulation_profiles[team_a]["att_vector"] * automatically_tuned_hfa_factor
                lambda_b = team_simulation_profiles[team_b]["att_vector"]
                if np.random.poisson(lambda_a) > np.random.poisson(lambda_b): current_iter_standings[team_a] += 3
                elif np.random.poisson(lambda_a) < np.random.poisson(lambda_b): current_iter_standings[team_b] += 3
                else: current_iter_standings[team_a] += 1; current_iter_standings[team_b] += 1
    winner_squad = max(current_iter_standings, key=current_iter_standings.get)
    simulated_championship_tally[winner_squad] += 1

st.markdown("---")
st.header("🏆 Divisional Outright Mass Entry Deck")
st.markdown("Type in the live outright odds from Hollywoodbets or Easybet for all teams simultaneously to refresh your ledger matrix.")

# Initialize a persistent dictionary memory cache for all team wagers safely
if "global_outright_odds_shelf" not in match_state:
    match_state["global_outright_odds_shelf"] = {team: 10.00 for team in all_teams_raw}

# Build a clean, multi-column entry deck that updates all at once
mass_entry_columns = st.columns(3)
for idx, team in enumerate(sorted(all_teams_raw)):
    target_col = mass_entry_columns[idx % 3]
    with target_col:
        saved_val = float(match_state["global_outright_odds_shelf"].get(team, 10.00))
        match_state["global_outright_odds_shelf"][team] = st.number_input(
            f"Odds: {team}", min_value=1.01, value=saved_val, step=1.00, key=f"mass_out_odds_input_{team.replace(' ', '_')}"
        )

# Compile the Upgraded 6-Column Outright Value Ledger Grid
st.markdown("##### 📊 Integrated 10,000-Iteration Outright Value Ledger")
outright_ledger_payload = []
for team in sorted(all_teams_raw):
    final_win_probability = simulated_championship_tally[team] / num_simulations_pass
    clamped_prob = max(0.001, final_win_probability)
    fair_zero_margin_odds = 1.0 / clamped_prob
    
    # 🟢 REAL-TIME SYNC: Reads your mass text inputs for every team all at once!
    live_bookie_odds = float(match_state["global_outright_odds_shelf"].get(team, fair_zero_margin_odds))
    outright_expected_value = (clamped_prob * live_bookie_odds) - 1.0
    
    outright_ledger_payload.append({
        "Competing Squad": team,
        "Model Win Probability (%)": f"{final_win_probability * 100:.1f}%",
        "Fair Value Odds Line": f"{fair_zero_margin_odds:.2f}",
        "Sportsbook Outright Odds": f"{live_bookie_odds:.2f}",
        "Model Edge (%)": f"{outright_expected_value * 100:+.1f}%",  # 🟢 OUTRIGHT EDGE COLUMN ACTIVE
        "Trading Outright Verdict": "🔥 FUTURES ALPHA" if outright_expected_value >= 0.05 else ("🛑 TRAP / FADE" if outright_expected_value <= -0.05 else "🔷 EFFICIENT HOLD")
    })

outright_master_df = pd.DataFrame(outright_ledger_payload)
st.dataframe(outright_master_df.sort_values(by="Model Win Probability (%)", ascending=False), use_container_width=True, hide_index=True)

# ==============================================================================
# SEGMENT 14: THE LIVING BETSLIP & FRACTIONAL RISK MANAGER SYSTEM
# ==============================================================================
st.markdown("---")
st.subheader("🎟️ Living Automated Betslip Layer")

# Extract the absolute most conservative probability entry row to protect capital
safe_baseline_record = market_payload_records[0]
ui_slip_market = safe_baseline_record["Derivative Trading Market"]
ui_slip_odds = float(safe_baseline_record["Sportsbook Live Odds"])
ui_slip_prob = float(safe_baseline_record["Monte Carlo Prob"].replace("%","")) / 100.0

# Calculate fractional stake parameters safely using a quarter-kelly framework
fractional_kelly_ratio = ((ui_slip_prob * ui_slip_odds) - 1.0) / (ui_slip_odds - 1.0) if ui_slip_odds > 1 else 0.0
clamped_fractional_risk = max(0.0, min(0.05, fractional_kelly_ratio * 0.25))

st.info(f"**Selected Betting Target:** {ui_slip_market} | **Current Price Line:** `{ui_slip_odds:.2f}`")
st.warning(f"🛡️ **Safety Shield Intercept Guard Allocation Unit:** `{clamped_fractional_risk * 100:.2f}%` of master campaign trading portfolio balance sizes.")
