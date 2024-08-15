[Start-up guide](https://www.iaps-app.org/start-up-guide)

# 1. Start-up steps

## 1.1. Basic setup

1. **Build and install iAPS**  
    If you have another DIY loop app installed on your iPhone, please remove CGM and Pump from that app before you continue.
    
2. **Allow Notifications**
    If you want to customize iAPS notifications, go to Settings -> Notifications
    
3. **Add your CGM**  
    Then, force-quit and restart iAPS. Wait for iAPS to pick up CGM readings. It might take up to 15 minutes. Nightscout is not a valid CGM for looping.
    
- **Add your Pump**  
    Remember to select the right insulin type to get an accurate insulin curve.
    
- **Add Nightscout (****optional****)  
    **Nightscout is not required for iAPS to work. However, it is a great tool for reporting and remote features.
    
- **Add Apple Health (optional)  
    **Apple Health is not required for iAPS to work. However, it is a great tool for reporting.
    
- **Add Basal Profile  
    **If you are uncertain, consult your endo or diabetes nurse. More information [here](https://iaps.readthedocs.io/en/main/settings/configuration/basalprofile.html).
    
- **Set your Target Glucose  
    **If you are uncertain, consult your endo or diabetes nurse. More information [here](https://iaps.readthedocs.io/en/main/settings/configuration/targetranges.html).
    
- **Add Insulin Sensitivities (ISF)**  
    If you are uncertain, consult your endo or diabetes nurse.
    
- **Add Carb Ratios (CR)**  
    If you are uncertain, consult your endo or diabetes nurse. More information [here](https://iaps.readthedocs.io/en/main/settings/configuration/carbratios.html).
    
- **Select Glucose Units**  
    Default is mmol/L; change to mg/dL if needed.
    
- **Set your Recommended Bolus Percentage**  
    This number will be applied as a factor in the bolus recommendations. A number below 100% will limit the bolus recommendation. More information [here](https://iaps.readthedocs.io/en/main/settings/configuration/preferences/freeapsx.html#recommended-bolus-percentage).
    
- **Set your Max Basal and Max Bolus in Pump Settings**  
    Max Basal is a limitation that ensures iAPS will never set a higher basal rate. Max Bolus is a limitation that ensures iAPS will not administer a bolus higher than this. There are several other limiting factors, but these are hard limits that will never be automatically exceeded. More information [here](https://iaps.readthedocs.io/en/main/settings/configuration/pumpsettings.html#delivery-limits).
    
- **Raise Max IOB**  
    to allow iAPS to dose insulin. This is a hard limit. If IOB is above this limit, iAPS will not automatically dose insulin. There are several other limiting factors, but these are hard limits that will never be automatically exceeded. More information [here](https://iaps.readthedocs.io/en/main/settings/configuration/preferences/mainsettings.html#max-iob).
    
- **Check Bolus Increment  
    **Default is 0.1U. Omnipod and Medtronic x22 use 0.05U. Medtronic x23 uses 0.025U.
    
- **Enable SMB**
    
    - With COB  
        (_iAPS is allowed to give SMBs when there are carbs entered and onboard_ )
        
    - With Temp Target  
        _(iAPS is allowed to give SMBs when there is a temporary target)_
        
    - After Carbs  
        _(iAPS is allowed to give SMBs after carbs are added_ )
        
    - With High BG  
        (_iAPS is allowed to give SMBs when BG is high, as defined by the setting “...When Blood Glucose is over (mg/dl)”. Note that this setting is in mg/dl! Default is 110 mg/dl._)
        
- **Change the Max Delta-BG Threshold SMB to 0.3**  
    to allow iAPS to use SMB when BG is rising quickly.
    
- **Enable UAM**  
    to allow iAPS to detect unannounced meals and dose insulin when needed.
    
- **Do not enable any Dynamic Settings yet!  
    **iAPS needs time to accumulate data before the dynamic features can work properly.
    
- **Close Loop**
    
- **Change your app icon in Preferences** 🙂
    

You should now see that iAPS is looping every 5 minutes. The loop circle should be green, adjusting your basal rates and giving you SMBs.

The prediction lines in iAPS should be ignored for the first 24 hours. They do not have adequate data to be reliable. They are only used in dynamic calculations. For this reason, do not turn on dynamic settings in the first 24 hours.

**In the first 24 hours**, iAPS will likely keep lows away, and the night will be awesome. Meals and highs, however, will be hard to handle without manual intervention. You should enter carbs and bolus for meals. Use the “Bolus” feature to add the insulin you need if your BG is high. No need to add fake carbs to treat highs. **Wait 24 hours** while iAPS gathers enough information about your BG and TDD (Total Daily Insulin Dosage). This information is necessary before enabling dynamic features.

# 2. Q&A and Scenarios
## 2.1. [What does iAPS have that Loop doesn’t?](https://iaps.readthedocs.io/en/latest/Configuration/transition-qa.html#what-does-iaps-have-that-loop-doesn-t)
- Unannounced meals
- Less user interaction / correction
- Dynamic ISF and IC
- Profile presets
## 2.2. [Why should I switch from Loop to iAPS?](https://iaps.readthedocs.io/en/latest/Configuration/transition-qa.html#why-should-i-switch-from-loop-to-iaps)

If Loop is working well for you, you should not switch to iAPS. If you’re having difficulties building the Loop app, you will have issues building iAPS. If you find it hard to understand how Loop works, you will find that iAPS is even more complex. You should consider switching to iAPS if you’ve been using Loop for a while and you have issues that Loop can’t solve even after tweaking and re-tweaking your settings and profile. [Common issues include](https://iaps.readthedocs.io/en/latest/Configuration/transition-qa.html#how-does-iaps-deal-with-those-common-issues):

1. Incorrect or missing carb entries
	*Unannounced Meals (BG rise when COB = 0)*
1. Lots of manual corrections and “fake carbs” 
	*No need to add "fake carbs"*
1. Persistent highs because of variations in insulin sensitivity (ISF) and insulincarb ratio (IC)
	*With dynamic ISF and dynamic IC enabled and properly configured, iAPS will give enough insulin to get those highs down*
4. Recurring/rebound lows
	*iAPS will not overcompensate for the rapid BG rise after a low.*
5. Difficulties dealing with exercise
	 *iAPS has a built-in exercise mode that will reduce basal, ISF and IC whenever you set a higher temporary BG target. iAPS also has Profile Presets that can help get the right amount of insulin during exercise.*
6. Frequent, consistent variations in profile (basal, ISF, IC)
	*iAPS has Profile Presets that can be used to change basal rate, ISF, IC and target BG in difference situations such as Illness, Menstrual cycle, Lazy days, Active days, Home office days,...*

## 2.3. Scenarios 1: Rollercoaster

![[rollercoaster.png]]

Đường huyết lên cao rồi lại xuống thấp, không ổn định in range --> ISF đang quá thấp, khiến lượng tiêm insulin quá nhiều hơn mức cần thiết ---> **cần giảm ISF**
## 2.4. Scenarios 2: staying high

![[stayhigh.png]]

Đường huyết có xu hướng từ từ đi lên cao:
- Nếu chỉ xảy ra sau ăn ---> lượng carb cần nhiều hơn Insulin ---> **giảm CR ( 1 UI hấp thụ ít hơn số carb)**
- Nếu xảy ra sau khi nhịn ăn trong 1 khoảng thời gian --> liều basal chưa đủ --> **tăng basal rate**
## 2.5. Scenarios 3: spike too high after meals

![[high_after_meal.png]]

Đường huyết lên cao và nhọn sau bữa ăn:
- Nếu 1-2H sau bữa ăn quay về in-range: --> **Vấn đề là thời điểm tiêm quá muộn**
	- *Tiêm sớm hơn trước bữa ăn*
	- *Sử dụng pre-bolusing (pre-meal)*
	- *Enable SMBs / UAM SMBs hoặc thay đổi limit value SMBs*
- Nếu 3H sau bữa ăn không quay về in-range : --> **Vấn đề liên quan đến insulin** 
	- *Giảm CR*
	- *Tăng basal rate*
	- *Sử dụng UAM SMBs*

# 3. Mealtime Strategy
1. Enable Pre-meal mode (keep lower target BG range)
1. Use the bolus calculator before eat:
	1. enter carbs (may be enter the future carbs if have infomations : fat + protein)
	2. change the recommendation if you want to, then bolus 
2. Eat after dosing:

| Eat after dosing | low BG state (<90) | normal BG state (90-130) | high gb state (>130) |
| ---- | ---- | ---- | ---- |
| slow carbs (>=3h) |         -10m | 0m | 15m |
| normal carbs (1-3h)  | 0m | 15m | 30m |
| fast carbs (<1h) | 5m | 30m | 45m |
> **breakfast + dinner**: dose 15m-30m before eat 
> **lunch**: dose when start gym 

1. After eat, if iAPS detect BG rising faster or more than expected, it will give more insulin (by SMB)
2. iAPS detect BG falling, then it keep low/zero temporary basal 
> - **low-carb meals**: not enter carbs
> - **high-carb meals**: pre-meal + enter carbs 

# 4. Settings 

## 4.1. Basic settings 

### 4.1.1. [Autotune](https://iaps.readthedocs.io/en/latest/settings/configuration/autotune.html#how-does-it-work)

Analyze the last 24h of data to adjust the basal rates (max 20% last 24h), ISF (max 10% last 24h), CR (max 10% last 24h) of the current parameters, 

The output is the predicted ratio, that also limited by `autosens` max/min, base on a statistical regression (not AI/ML) use the deviation of basal rate, ISF, CR and adjust maximum 10% of change to get that deviation to 0

> Autotune results can be unreliable if dynamic settings are enabled.

**Compare with autosens**
	- Autosens thiết kế cho những thay đổi liên tục dựa trên data gần đây, phản ánh nhanh chóng và dựa trên vả vị trí tiêm
	- Autotune hoạt động dựa trên data trong thời gian dài, thay đổi mỗi 24h, với mục tiêu là đưa tham số profile chính xác hơn.

**Should I enable Autotune**
	- Hãy bật khi thấy profile được cài đặt chưa đúng hoặc đã có sự thay đổi do: thể trạng cơ thể thay đổi, bị ốm, hoạt động hằng ngày thay đổi,...
	- Autotune bị giới hạn bởi autosens max/min ratios
	- Các giá trị trong profile sẽ được tự động thay đổi để phù hợp hơn --> hãy review lại tham số sau 1 tháng và lưu lại backup

### 4.1.2. [Basal Profile](https://iaps.readthedocs.io/en/latest/settings/configuration/basalprofile.html)

Liều nền Basal rate là lượng insulin cần thiết để duy trì mức GB ổn định hằng giờ ( nếu ko có liều basel thì các hoocmon khác trong cơ thể sẽ làm GB tăng, mặc dù không bổ sung carbs do ăn)

Basal rate ảnh hưởng đến xác định lượng IOB:
- Nếu lượng Insulin tiêm vào cơ thể lớn hơn Basal rate thì sẽ tạo ra `high temporary basal rates` hoặc xuất hiện liều bolus --> Khi đó **IOB > 0**
- Nếu lượng Insulin tiêm vào cơ thể nhỏ hơn Basal rate hoặc bằng 0 thì sẽ tạo ra `low temporary basal rates` --> Khi đó **IOB <= 0** 
	- negative IOB tức là liều `basal` đang không được tiêm vào cơ thể
	- IOB = 0 tức là không có liều `bolus` hay là `high temporary basal rates`, chỉ đang có liều `Basal tiêu chuẩn` được tiêm vào cơ thể

**Setup Basal profile**
- Transfer from pump
- Xác định sự chính xác của liều Basal bằng cách nhịn ăn trong nhiều giờ (COB = 0), đáng giá sự thay đổi của GB
- Xác định Basal dựa trên giá trị IOB theo các thời điểm trong ngày tại nhiều ngày
	- Nếu buổi đêm, IOB luôn ở trạng thái dương --> **Basal đang thiếu --> tằng basal buổi đêm**
	- Nếu tại 1 thời điểm nhất định trong ngày, IOB luôn âm, tức là lượng Insulin đang dư thừa
- Sử dụng autotune:
	- Review hằng ngày xu hướng điều chỉnh giá trị basal profile

### 4.1.3. [Insulin Carbohydrate Ratio - CR](https://iaps.readthedocs.io/en/latest/settings/configuration/carbratios.html)

CR refer to the amount of carbohydrates one UI of insulin is able to neutralize. Normally, CR is not changed as drastically (like basal rate or ISF)

**Setup CR**
- Transfer from pump settings 
- Test meal experiment with not loop: meal with known carbs and bolus with current CR. Then check the BG at 3 hour mark
- Autotune enable then change the value if trend value stabilizes

### 4.1.4. Safety limiters

- Max Basal = 4x max daily basal = 3
- Max Bolus = Max bolus you give for a meal = 10
- Max Carbs = Maximum carbs allowed by a single entry = 100
- DIA = Duration of Insulin Action (typically 6-7 hours)

### 4.1.5. Target glucose

- Set your target glucose between 5-6 mmol/L (90-110 mg/dL)
- May be higher during night to avoid lows

### 4.1.6. Fat and Protein Conversion

Fat and protein may tend to slow rises in BG (future carbs), then need to delay bolus for fat & protein (**FPU**)

Enable the **Convert Fat & Protein**:
- **Delay in minutes (60m)** : how long the system start bolus after meals for the fat & protein spike
- **Maximum duration in hours (8 hours)**: how long system can bolus for FPU
- **Interval in Minutes**: Interval between each microbolus provided for fat and protein.
- **Override With A Factor Of (0.5)**: tỷ lệ delivery insulin cho FPU, nếu thấy BG rise do Fat and Protein thì hãy tăng giá trị này

> If you choose to enable this setting, you will need to make your ICR less aggressive (higher CR) to prevent lows.
### 4.1.7. Carbs Required Threshold

The minimum amount of carbs required (mark as threshold) to avoid risk of having a low blood sugar event
## 4.2. Advanced settings 

### 4.2.1. Autosens

React the sensitive level of insulin by the lastest 8-24h data, then adjust temporary Basal rate, GB target and ISF. Autosens does not look at the meals and make adjustments to CR.

> Nếu sử dụng autotune, autosens tính toán các thông số dựa trên các chỉ số CR, ISF, Basal rate của autotune thay vì các chỉ số mặc định set ban đầu

### 4.2.2. Dynamic ISF

`Dynamic ISF` is more aggressive than autosens to make change the ISF (turn it on if ISF has a high variance)
- Increase **Adjustment Factor** to make **Dynamic ISF** more aggressive



> **Dynamic ISF** is disabled (revert to autosens) when active `High Temptarget Raises Sensitivity` or `Exercise Mode`

