import streamlit as st

def calculate_fuel_required(boiler_production_rate_ton, enthalpy_steam, enthalpy_water, boiler_efficiency, gas_calorific_value_btu_ft3):
  """
  Calculates the fuel required to produce steam.

  Args:
    boiler_production_rate_ton: The production rate of the boiler in tons.
    enthalpy_steam: The enthalpy of the steam in kilojoules per kilogram.
    enthalpy_water: The enthalpy of the water in kilojoules per kilogram.
    boiler_efficiency: The efficiency of the boiler as a fraction.
    gas_calorific_value_btu_ft3: The calorific value of the gas in Btu per cubic foot.

  Returns:
    The fuel required in cubic meters, or None if there's a division by zero error.
  """
  # Conversion factors
  kg_per_ton = 1000
  kilojoules_per_btu = 1.055
  cubic_meters_per_ft3 = 0.0283168

  # Convert production rate ton to kg
  boiler_production_rate_kg = boiler_production_rate_ton * kg_per_ton

  # Convert Btu/ft³ to J/m³
  gas_calorific_value_kj_m3 = gas_calorific_value_btu_ft3 * kilojoules_per_btu / cubic_meters_per_ft3

  try:
    fuel_required = boiler_production_rate_kg * (enthalpy_steam - enthalpy_water) / (boiler_efficiency * gas_calorific_value_kj_m3)
    return fuel_required
  except ZeroDivisionError:
    return None  # Handle division by zero

st.title("Boiler N.G Fuel Calculator")
st.caption("By Eng. Ali Jabbar Mezeal @ http://utility.src.net")

# Get User Input with container
with st.container():
  boiler_efficiency = st.number_input("Boiler Efficiency", min_value=0.0, max_value=1.0,value=0.9)
  boiler_production_rate_ton = st.number_input("Boiler Steam Production Rate (ton)", min_value=0.0,value=50.0)
  enthalpy_steam = st.number_input("Enthalpy of Steam Outlet (kJ/kg)", min_value=0.0,value=3230.0)
  enthalpy_water = st.number_input("Enthalpy of Water Input (kJ/kg)", min_value=0.0,value=615.0)
  gas_calorific_value_btu_ft3 = st.number_input("Fuel Gas Calorific Value (Btu/ft³)", min_value=0.0,value=1100.0)

if st.button("Calculate"):
  fuel_required = calculate_fuel_required(boiler_production_rate_ton, enthalpy_steam, enthalpy_water, boiler_efficiency, gas_calorific_value_btu_ft3)
  if fuel_required is not None:
    st.info(f"Approximately Fuel Required: {fuel_required:.2f} m3 ")
  else:
    st.error("Error: check inputs values not zero ! ")
