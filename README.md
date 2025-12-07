# Pokémon Battle Prediction: Sức mạnh của Data Preparation qua Data Storytelling

Report: https://drive.google.com/file/d/1jGN4OU0_YpOQZ-LmI9o0witapJb3Sjxv/view?fbclid=IwY2xjawOinkNleHRuA2FlbQIxMQBzcnRjBmFwcF9pZAEwAAEeRmtTtm04iNKmuXbiZgQrcH4HqeQoqilXN5Zcm4UFcLlG7-lFFYCtb1TjkCA_aem_8qJKkR35RskcBO2W_VVAYw&pli=1

## 1. Bối cảnh & mục tiêu của dự án

Pokémon là một franchise game xoay quanh việc thu thập và huấn luyện các sinh vật gọi là Pokémon để thi đấu với nhau. 

Bài toán được đặt ra như sau:

> Dựa trên các đặc điểm của hai Pokémon, liệu chúng ta có thể dự đoán được Pokémon nào sẽ thắng trong một trận đấu không?

Dự án này được thực hiện như một minh chứng cho sự hiệu quả của quá trình chuẩn bị dữ liệu (Data Preparation) thông qua nghệ thuật kể chuyện với dữ liệu (Data Storytelling), khẳng định rằng việc hiểu bối cảnh dữ liệu quan trọng hơn việc chỉ chạy các thuật toán máy móc.

## 2. Dữ liệu sử dụng

Nguồn dữ liệu: 
- **[Pokemon - Weedles's Cave](https://www.kaggle.com/datasets/terminus7/pokemon-challenge/data)**
- **[Bulbapedia](https://bulbapedia.bulbagarden.net/)**

Các bộ dữ liệu gốc:
- `pokemon.csv`: Chứa thông tin cơ bản về các Pokémon, bao gồm các chỉ số cơ bản như HP, Attack, Defense, Speed, v.v.
- `combats.csv`: Chứa thông tin về kết quả trận đấu giữa các Pokémon, bao gồm ID của hai Pokémon tham gia và ID của Pokémon chiến thắng.
- `pokemonfullstats.csv`: Chứa thông tin chi tiết hơn về các chỉ số của Pokémon, được scrape từ Bulbapedia.

## 3. Cấu trúc repo
```
.
├─ Images
│  ├─ Graphics 
│  │  # Biểu đồ 
│  └─ Icons 
│     # Biểu tượng của các Pokémon
│
├─ data
│  ├─ modified 
│  │  # Dữ liệu đã được xử lý
│  └─ raw_data 
│     # Dữ liệu gốc
│
├─ notebooks
│  ├─ 1_Data_Understanding.ipynb 
│  │  # Tìm hiểu về các biến của dữ liệu
│  ├─ 2_Data_Preprocessing.ipynb 
│  │  # Tiền xử lý dữ liệu
│  ├─ 3_Data_Exploration.ipynb 
│  │  # Khám phá và làm sạch dữ liệu
│  ├─ 4_Clean_Data_Visualization.ipynb 
│  │  # Trực quan hóa dữ liệu sạch
│  └─ 5_FE&Model.ipynb 
│     # Feature Engineering và xây dựng mô hình
│
├─ README.md 
│  # Tài liệu hướng dẫn dự án
│
├─ Scrapper.py 
│  # chương trình scrape dữ liệu từ Bulbapedia
│
└─ requirements.txt 
   # Thư viện cần thiết để chạy các notebook
```

## 4. Hướng dẫn

### Yêu cầu môi trường

- Python 3.12
- Thư viện: Xem chi tiết trong `requirements.txt`

### Thứ tự chạy các notebook

1. `1_Data_Understanding.ipynb`: Tìm hiểu về các biến của dữ liệu

2. `2_Data_Preprocessing.ipynb`: Tiền xử lý dữ liệu

3. `3.Data_Exploration.ipynb`: Khám phá và làm sạch dữ liệu

4. `4_Clean_Data_Visualization.ipynb`: Trực quan hóa dữ liệu sạch

5. `5_FE&Model.ipynb`: Feature Engineering và xây dựng mô hình
