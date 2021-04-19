import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

# st.write('DataFrame')
st.write('Display Image')

img = Image.open('nora.png')
st.image(img, caption='Kohei Imanishi', use_column_width=True)



# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40],
# })

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
# st.dataframe(df.style.highlight_max(axis=0))
# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))

# st.dataframe(df)

# df = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c']
# )
# df = pd.DataFrame(
#     np.random.randn(100, 2)/[50,50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.dataframe(df.style.highlight_max(axis=0))
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)
# st.map(df)



# """
# # 章
# ## 節
# ### 項
#
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """
