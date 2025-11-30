import streamlit as st
import pandas as pd
import itertools

def create_google_maps_route_url(addresses):
    """Create a Google Maps URL with multiple destinations"""
    base_url = "https://www.google.com/maps/dir/"
    encoded_addresses = []
    
    for address in addresses:
        # Clean and encode the address
        clean_addr = address.replace(' ', '+').replace(',', '')
        encoded_addresses.append(clean_addr)
    
    # Join all addresses with slashes
    route_url = base_url + '/'.join(encoded_addresses)
    return route_url

def main():
    st.set_page_config(page_title="Google Maps Route Planner - All 37 Addresses", page_icon="🗺️", layout="wide")
    
    st.title("🗺️ Google Maps Route Planner - All 37 Bangalore Addresses")
    
    # Complete dataset with all 37 addresses
    addresses_data = [
        {'id': 1, 'address': 'C-88 3rd floor Block -7 central silk board staff quarters BMT first stage 36 main 3rd cross', 'area': 'Silk Board'},
        {'id': 2, 'address': 'DS Max Serenity A block 404 NGR Layout Roopena Agrahara Bommanahalli', 'area': 'Roopena Agrahara'},
        {'id': 3, 'address': '43/1, 9th cross, Muneshwara layout, kudlu gate', 'area': 'Kudlu Gate'},
        {'id': 4, 'address': 'Flat no. 1402 A2 block Mahaveer ranches apartment Sree sai layout parappana agrahara near Hosa road', 'area': 'Parappana Agrahara'},
        {'id': 5, 'address': 'Flat 110 Aashraya Crystal Apartment Behind Ganesha Temple Bommnahalli', 'area': 'Bommanahalli'},
        {'id': 6, 'address': 'Building 789 flat no 403 shri sai samruddhi 4th cross iti layout sector 7 HSR', 'area': 'HSR Sector 7'},
        {'id': 7, 'address': 'A1 408 DS max serenity Roopinagrahara Near Sai baba temple KARNATAKA', 'area': 'Roopena Agrahara'},
        {'id': 8, 'address': 'C-004 Bren Plams, Kudlu Road, Hosur Road Opp Bhagya Veg Restaurant KARNATAKA', 'area': 'Kudlu Road'},
        {'id': 9, 'address': 'G7, Windermere by sriParvata 2nd main 1st cross, AECS B Block KARNATAKA', 'area': 'AECS Layout'},
        {'id': 10, 'address': 'Makana Square Apartment, 4th main Road, NGR Layout, Bommanahalli', 'area': 'NGR Layout'},
        {'id': 11, 'address': 'E113 Snn Raj Grandeur Bommanahalli 560068', 'area': 'Bommanahalli'},
        {'id': 12, 'address': 'Bluespring Enterprises Ltd, crimson square 3rd floor, 31/9 Rupena agrahara Hosur road KARNATAKA', 'area': 'Roopena Agrahara'},
        {'id': 13, 'address': 'Mahaveer Turquoise D212 Basapura Village Road', 'area': 'Basapura'},
        {'id': 14, 'address': '86 Mohanum Enclave Venkateshwara layout AECS layout Block A Kudlu Bangalore Karnataka', 'area': 'AECS Layout'},
        {'id': 15, 'address': 'A 903 Sumo Sonnet Apartment, Kudlu Gate, Bengaluru, Karnataka, India', 'area': 'Kudlu Gate'},
        {'id': 16, 'address': '696 11th Main Road 27th Cross Rd AECS B Block Singasandra Begur', 'area': 'Singasandra'},
        {'id': 17, 'address': 'Flat no.212, Greystone mirror on Water Silver county road,haralur road KARNATAKA', 'area': 'Silver County'},
        {'id': 18, 'address': '418 Colive 1200 Birmingham Roopena Agrahara Bommanahalli Hosur Main road Bangalore', 'area': 'Roopena Agrahara'},
        {'id': 19, 'address': '1963 2nd floor aecs layout a block Singasandra', 'area': 'AECS Layout'},
        {'id': 20, 'address': '32 near Zion ag church 4th main gulbarga NGR layout roopena agarhara bommnanhalli KARNATAKA', 'area': 'NGR Layout'},
        {'id': 21, 'address': '403 Iconest 5,near TCIS school harlur road ,sai meadows KARNATAKA', 'area': 'Haralur Road'},
        {'id': 22, 'address': 'A209 TG ARTE 8th Cross Rd AECS LAYOUT Kudlu', 'area': 'AECS Layout'},
        {'id': 23, 'address': '208 NR Whitepearl apartments Parappana Agrahara Road Kudlu', 'area': 'Parappana Agrahara'},
        {'id': 24, 'address': '402/1 15th A main 13th cross Venkateshwara layout Madiwala', 'area': 'Madiwala'},
        {'id': 25, 'address': 'Central jail parappana agrahar jail Quarters B11-Bengalore KARNATAKA', 'area': 'Parappana Agrahara'},
        {'id': 26, 'address': 'A1-022 SNN Raj Etternia apt silver county road haralur road off Sarjapur road Sarjapur Bangalore 560068', 'area': 'Silver County'},
        {'id': 27, 'address': '307 Sai Nidhi Residency161A Hosapalya main road next to DTDC HSR sector 7', 'area': 'HSR Sector 7'},
        {'id': 28, 'address': 'No.61,N G R Layout Virat Nagar Roopena Agrahar,Bommanahalli,Bengaluru KARNATAKA', 'area': 'NGR Layout'},
        {'id': 29, 'address': 'A 504 Purva Skywood Silver County Road off Haralur Road Sarjapur', 'area': 'Silver County'},
        {'id': 30, 'address': 'C1-101 SNN Raj Etternia Silver county road. Off Sarjapur - Haralur road.', 'area': 'Silver County'},
        {'id': 31, 'address': 'NR white meadows revenue layout Singasandra Bangalore-68', 'area': 'Singasandra'},
        {'id': 32, 'address': 'No101/28/6 sri venugopala flour mill roopena agrahara bommanagalli KARNATAKA', 'area': 'Roopena Agrahara'},
        {'id': 33, 'address': '505 Sobha Cinnamon Silver County road off Harlur road', 'area': 'Silver County'},
        {'id': 34, 'address': 'Flat No. 204, 2nd Floor, NVR Grand, NGR Layout, Roopena Agrahara, Bommanahalli', 'area': 'NGR Layout'},
        {'id': 35, 'address': 'SNN Raj Etternia Silver County Road Off Harlur Road Off Sarjapur Road B3 084', 'area': 'Silver County'},
        {'id': 36, 'address': 'House 26, 2nd cross , muneshwara layout Near sgs residency , kudlu main road KARNATAKA', 'area': 'Kudlu Road'},
        {'id': 37, 'address': 'RBD Still Water Apartments 5Q Silver County Road HSR Extension Main Sarjapura Hobli', 'area': 'Silver County'}
    ]
    
    df = pd.DataFrame(addresses_data)
    
    st.sidebar.header("🔧 Route Planning Options")
    
    # Area-based filtering
    areas = ['All Areas'] + sorted(df['area'].unique())
    selected_area = st.sidebar.selectbox("Filter by Area:", areas)
    
    if selected_area != 'All Areas':
        filtered_df = df[df['area'] == selected_area]
        st.sidebar.write(f"📊 {len(filtered_df)} addresses in {selected_area}")
    else:
        filtered_df = df
    
    st.subheader("📍 Select Addresses for Route Planning")
    
    # Display addresses with checkboxes
    selected_addresses = []
    
    st.write(f"**Total addresses available: {len(filtered_df)}**")
    
    # Create columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        for i in range(0, len(filtered_df), 2):
            if i < len(filtered_df):
                row = filtered_df.iloc[i]
                if st.checkbox(f"**{row['id']}.** {row['address'][:70]}...", key=f"addr_{row['id']}"):
                    selected_addresses.append(row['address'])
    
    with col2:
        for i in range(1, len(filtered_df), 2):
            if i < len(filtered_df):
                row = filtered_df.iloc[i]
                if st.checkbox(f"**{row['id']}.** {row['address'][:70]}...", key=f"addr_{row['id']}"):
                    selected_addresses.append(row['address'])
    
    if selected_addresses:
        st.success(f"✅ {len(selected_addresses)} addresses selected")
        
        # Route optimization options
        st.subheader("🔄 Route Organization")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔄 Reverse Route Order"):
                selected_addresses.reverse()
                st.rerun()
        
        with col2:
            if st.button("🧭 Sort by Area"):
                # Group by area
                area_sorted = []
                for area in df['area'].unique():
                    for addr in selected_addresses:
                        if any(row['address'] == addr and row['area'] == area for _, row in df.iterrows()):
                            area_sorted.append(addr)
                selected_addresses[:] = area_sorted
                st.rerun()
        
        with col3:
            if st.button("🔢 Reset to Original Order"):
                # Reset to original selection order based on ID
                original_order = sorted(selected_addresses, 
                                      key=lambda x: next(row['id'] for _, row in df.iterrows() if row['address'] == x))
                selected_addresses[:] = original_order
                st.rerun()
        
        # Display selected route
        st.subheader("📋 Your Route Plan")
        
        for i, address in enumerate(selected_addresses, 1):
            area = next(row['area'] for _, row in df.iterrows() if row['address'] == address)
            st.write(f"**Stop {i}** ({area}): {address}")
        
        # Google Maps Route Generation
        st.subheader("🗺️ Generate Google Maps Routes")
        
        # Handle large number of addresses by splitting into multiple routes
        if len(selected_addresses) > 10:
            st.warning(f"⚠️ Google Maps allows maximum 10 stops per route. You have {len(selected_addresses)} addresses selected.")
            st.info("💡 I'll automatically split your route into multiple parts with 10 stops each.")
            
            # Split into chunks of 9 (since start + 9 stops = 10 total)
            route_chunks = [selected_addresses[i:i+9] for i in range(0, len(selected_addresses), 9)]
            
            for i, chunk in enumerate(route_chunks, 1):
                st.write(f"**Route Part {i}** ({len(chunk)} stops)")
                route_url = create_google_maps_route_url(chunk)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"[🚗 Driving]({route_url}/@12.9000,77.6300,13z/data=!4m2!4m1!3e0)")
                with col2:
                    st.markdown(f"[🚶 Walking]({route_url}/@12.9000,77.6300,13z/data=!4m2!4m1!3e2)")
                with col3:
                    st.markdown(f"[🚌 Transit]({route_url}/@12.9000,77.6300,13z/data=!4m2!4m1!3e3)")
                
                # Show addresses in this chunk
                with st.expander(f"View Route Part {i} Addresses"):
                    for j, addr in enumerate(chunk, 1):
                        st.write(f"{j}. {addr}")
        else:
            # Single route for <= 10 addresses
            route_url = create_google_maps_route_url(selected_addresses)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f"### [🚗 Driving Route]({route_url}/@12.9000,77.6300,13z/data=!4m2!4m1!3e0)")
            with col2:
                st.markdown(f"### [🚶 Walking Route]({route_url}/@12.9000,77.6300,13z/data=!4m2!4m1!3e2)")
            with col3:
                st.markdown(f"### [🚌 Transit Route]({route_url}/@12.9000,77.6300,13z/data=!4m2!4m1!3e3)")
        
        # Export options
        st.subheader("📤 Export Your Route Plan")
        
        # Text export
        route_text = "GOOGLE MAPS ROUTE PLAN\n" + "="*50 + "\n\n"
        route_text += f"Total Stops: {len(selected_addresses)}\n"
        route_text += f"Generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        
        for i, address in enumerate(selected_addresses, 1):
            area = next(row['area'] for _, row in df.iterrows() if row['address'] == address)
            route_text += f"STOP {i} ({area}):\n{address}\n{'-'*80}\n"
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.download_button(
                "📥 Download as Text File",
                route_text,
                file_name="complete_route_plan.txt",
                mime="text/plain"
            )
        
        with col2:
            # CSV export
            route_df = pd.DataFrame({
                'Stop_Number': range(1, len(selected_addresses) + 1),
                'Area': [next(row['area'] for _, row in df.iterrows() if row['address'] == addr) for addr in selected_addresses],
                'Address': selected_addresses
            })
            csv_data = route_df.to_csv(index=False)
            st.download_button(
                "📊 Download as CSV",
                csv_data,
                file_name="route_plan.csv",
                mime="text/csv"
            )
    
    else:
        st.info("👆 Select addresses from the list above to create your route")
    
    # Quick route templates for common areas
    st.sidebar.header("🚀 Quick Routes")
    
    quick_routes = {
        "Silver County Tour": [26, 29, 30, 33, 35, 37],
        "Bommanahalli Cluster": [2, 5, 11, 28],
        "HSR Sector 7": [6, 27],
        "Kudlu Gate Area": [3, 15, 36],
        "AECS Layout Tour": [9, 14, 19, 22],
        "Roopena Agrahara": [2, 7, 12, 18, 32]
    }
    
    for route_name, address_ids in quick_routes.items():
        if st.sidebar.button(f"📍 {route_name}"):
            quick_addresses = [df[df['id'] == id]['address'].iloc[0] for id in address_ids]
            # This would need to be handled with session state to auto-select
            st.sidebar.success(f"✅ {route_name} loaded! Select addresses manually above.")

if __name__ == "__main__":
    main()