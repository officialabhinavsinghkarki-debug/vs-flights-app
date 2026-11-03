import streamlit as st
from dbhelper import DB

db = DB()

st.sidebar.title('Flights App')

user_option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')

    col1, col2 = st.columns(2)

    city = db.fetch_city_names()

    with col1:
        source = st.selectbox('Source',city)

    with col2:
        destination = st.selectbox('Destination',city)

    if st.button('Search'):
        st.write('Selected source:',source)
        st.write('Selected destination:',destination)

        results = db.fetch_all_flights(source,destination)

        if results:
            st.success(f"{len(results)} flights found")

            st.dataframe(results)
        else:
            st.warning('no flights found')

elif user_option == 'Analytics':
    st.title('Analytics')
    st.header('Flights Data Analytics')
    st.subheader('Number of flihgts per airline')
    airline_data = db.fetch_airline_frequency()
    if airline_data:
        airline_dict = {}
        for i in airline_data:
            airline_dict[i[0]] = i[1]
        st.bar_chart(airline_dict)

    else:
        st.info("no data available for airline frequence")

    st.divider()

    st.subheader('Average Ticket Price per Airline')
    price_data = db.fetch_airline_fare()
    if price_data:
        price_dict = {}
        for i in price_data:
            price_dict[i[0]] = float(i[1])
        st.bar_chart(price_dict)

    else:
        st.info('No data available for average prices')

    st.divider()

    st.subheader('Flight Departure by Source City')
    city_data = db.fetch_city_frequencey()
    if city_data:
        city_dict = {}
        for i in city_data:
            city_dict[i[0]] = i[1]
        st.bar_chart(city_dict)
    else:
        st.info('No data available for city frequency')
