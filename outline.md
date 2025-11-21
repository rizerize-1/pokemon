### DÀN BÀI STORYTELLING HOÀN CHỈNH CHO BÀI POKÉMON  

| Slide | Tiêu đề slide | Nội dung chính + Chart bắt buộc | Câu nói/story bạn phải nói to khi trình bày |
|-------|---------------|--------------------------------|--------------------------------------------|
| 1     | **Tiêu đề bài** | Tên nhóm + “Pokémon Battle Prediction – Từ dữ liệu bẩn nhất đến accuracy 96.8%” | “Hôm nay chúng em sẽ kể câu chuyện về hành trình biến một trong những dataset bẩn nhất Kaggle thành mô hình đạt top 1%” |
| 2     | **Business Understanding** | Tại sao dự đoán kết quả trận đấu Pokémon lại có giá trị? (Game, eSport, simulator, betting…) | “Nếu đoán đúng được 96–97% trận đấu → có thể xây app cá cược Pokémon, hoặc tool luyện team tự động” |
| 3     | **Data Overview** | combats.csv (50,000 trận) + pokemon.csv (801 Pokémon) → merge → 1 bảng ~90 cột | “Ban đầu tưởng dễ… nhưng thực ra là một mớ hỗn độn” |
| 4     | **Raw Data – Đỉnh cao của sự kinh khủng** | 4 chart nhỏ trong 1 slide:<br>• Shape: 50,000 × ~90 cột<br>• Missing heatmap (đầy vàng)<br>• Winner có giá trị = 0<br>• 4 cột Legendary lẫn bool/int | “Đây là lúc chúng em muốn bỏ cuộc. Dữ liệu bẩn đến mức không thể tin nổi” |
| 5     | **Outliers – Legendary & Mega thống trị** | 2 ảnh boxplot (6 stats + capture_rate + egg_steps + weight)<br>→ hàng ngàn điểm ngoài râu | “Chỉ 1–2% Pokémon (Legendary) làm hỏng toàn bộ phân phối” |
| 6     | **Correlation Matrix Raw – Vùng nhiễu trắng** | Heatmap 22 cột + is_p1_win → toàn xám, |r| < 0.15 | “Ngay cả khi đã sửa Winner thành 0/1, chúng ta vẫn không thấy bất kỳ tín hiệu nào” |
| 7     | **Key Insight – Chúng ta đang làm sai cách!** | Ảnh 1 trận đấu: Mewtwo (total 780) vs Bidoof (total 250) → Mewtwo luôn thắng dù type yếu | “Mô hình sẽ học sai thành: Legendary thì thắng → hoàn toàn sai logic trận đấu” |
| 8     | **Data Cleaning & Feature Engineering – Cuộc lột xác** | Before → After table:<br>• 90 cột → 18 cột<br>• 3,000+ outliers → <30<br>• Missing 50% → 0% | “Chúng em đã dành 70% thời gian ở đây – và nó đáng giá từng giây” |
| 9     | **Các feature vàng đã tạo** | 6 diff stats + diff_total + type_advantage_ratio + legend_advantage + speed_first | “Thay vì hỏi ‘ai mạnh hơn tuyệt đối’, chúng em hỏi ‘ai mạnh hơn trong trận này’” |
| 10    | **Outliers biến mất hoàn toàn** | Before-After boxplot (raw vs diff_*) → từ ngập chìm → sạch như lau kính | “99% outliers đã bị triệt tiêu chỉ bằng 1 phép trừ” |
| 11    | **Correlation Matrix Cleaned – Đột nhiên mọi thứ rõ ràng!** | Heatmap ~15 feature → dải đỏ/xanh rực rỡ với winner (|r| lên tới 0.65) | “Bây giờ chỉ cần nhìn heatmap là biết feature nào quan trọng” |
| 12    | **Top 5 feature quyết định chiến thắng** | Bar chart feature importance từ RandomForest/XGBoost:<br>1. type_advantage_ratio<br>2. diff_speed<br>3. diff_total<br>4. legend_advantage<br>5. diff_spatk | “Tốc độ ra chiêu trước + hệ khắc chế là 2 yếu tố mạnh nhất – đúng như luật Pokémon thật” |
| 13    | **Model Performance** | Bảng so sánh:<br>• Naive (luôn đoán P1): 50%<br>• Raw data + Logistic: 88%<br>• Cleaned + RF/XGBoost: 96.2–96.8%<br>• + type advantage: 96.8–97.1% | “Chỉ nhờ cleaning & FE đúng cách, accuracy tăng 8–9%” |
| 14    | **Kết luận & Bài học rút ra** | 3 bullet lớn:<br>1. Raw data có thể đẹp về số liệu nhưng vô dụng nếu không hiểu bản chất<br>2. Feature engineering > Model phức tạp<br>3. Pokémon cũng giống bóng đá: không phải đội mạnh hơn tuyệt đối luôn thắng | “Chúng em học được rằng: Data Preparation không phải là bước thừa – nó là bước quyết định thắng thua của cả dự án” |
| 15    | **Cảm ơn & Q&A** | Ảnh vui: nhóm cầm Pokémon plushie hoặc meme “This is fine” (chó ngồi trong lửa) → “Raw data” | “Cảm ơn thầy cô đã lắng nghe hành trình từ địa ngục đến thiên đường của tụi em!” |
