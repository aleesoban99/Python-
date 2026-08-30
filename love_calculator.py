def name(male,female):
    true_count=(male.count("l"))+(male.count("o"))+ (male.count("v"))+ (male.count("e"))
    love_count=(male.count("t"))+(male.count("r"))+ (male.count("u"))+ (male.count("e"))
    male_final=true_count+love_count

    
    love_count1=(female.count("l"))+(female.count("o"))+ (female.count("v"))+ (female.count("e"))
    true_count1=(female.count("t"))+(female.count("r"))+ (female.count("u"))+ (female.count("e"))
    female_final=true_count1+love_count1
   

    print(f"Your True love is {male_final}{female_final}%")

name(male="Saul ",female="kimberly ")