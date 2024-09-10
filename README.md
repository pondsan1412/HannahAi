# HannahAi - Discord Bot Project

![image](https://github.com/user-attachments/assets/df881391-da5e-4349-8a8f-419e3bf40cee)
 
*(ภาพประกอบ: HannahAi - บอท Discord ที่ถูกสร้างขึ้นมาให้เพื่อนๆ ใช้ในเซิร์ฟเวอร์เดียว)*

## เกี่ยวกับโปรเจค
**HannahAi** เป็นโปรเจค Discord Bot ที่ออกแบบมาเพื่อใช้งานในกลุ่มเพื่อนๆ ในเซิร์ฟเวอร์เดียว มีความสามารถหลากหลาย สามารถปรับแต่งและพัฒนาได้ตามความต้องการของกลุ่ม ด้วยการทำงานของ bot จะเป็นแบบ custom ทั้งในด้านการทำงานและการเชื่อมต่อกับ API ภายในของโปรเจค

### ภาษาและเครื่องมือที่ใช้
- **ภาษา**: Python, PHP
- **Library ที่ใช้**:
  - [discord.py](https://discordpy.readthedocs.io/)
  - [requests](https://docs.python-requests.org/)
  - [mysql2](https://github.com/sidorares/node-mysql2)
  
- **Backend**: PHP เชื่อมต่อกับ API ภายใน
- **ฐานข้อมูล**: ใช้ phpMyAdmin ที่รันอยู่บน localhost
![image](https://github.com/user-attachments/assets/4f7a8a0f-22f2-4a16-b093-70066c5f77c3)

## วิธีการติดตั้งและใช้งาน

1. **Clone Repository**  
   ```bash
   git clone https://github.com/username/HannahAi.git
   cd HannahAi
   ```

2. **ติดตั้ง Dependencies**  
   รันคำสั่งต่อไปนี้เพื่อติดตั้ง dependencies ที่จำเป็นสำหรับโปรเจค
   ```bash
   pip install -r requirements.txt
   ```

3. **ตั้งค่า API และ Database**  
   - ตรวจสอบให้แน่ใจว่ามี phpMyAdmin รันอยู่บน localhost และเซ็ตค่าการเชื่อมต่อฐานข้อมูลในไฟล์ `config.php`
   - รัน API ภายในของโปรเจคบน localhost ด้วย PHP

4. **การใช้งานบอท**  
   ใช้ token ของ Discord Bot และนำไปใส่ในไฟล์ `.env`
   ```env
   DISCORD_TOKEN=your_discord_token
   ```

5. **รันโปรเจค**  
   เมื่อเซ็ตอัพทุกอย่างเสร็จเรียบร้อย สามารถรันโปรแกรมได้โดยใช้คำสั่ง:
   ```bash
   python bot.py
   ```

## ข้อมูลเพิ่มเติม
บอทตัวนี้สามารถพัฒนาและปรับแต่งได้ตามความต้องการ โดยสามารถเชื่อมต่อกับ API และฐานข้อมูลเพื่อเพิ่มฟังก์ชันการทำงานใหม่ๆ ได้

## ภาพรวมการทำงาน
![ภาพประกอบ](./path-to-image-2.png)  
*(ภาพแสดงการทำงานของบอทเชื่อมต่อกับ API และฐานข้อมูล)*
