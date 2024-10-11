import pandas as pd

def compare_and_save_matching_emails(data_file, form_file, output_file):
    # 두 엑셀 파일 읽기
    data_df = pd.read_excel(data_file)
    form_df = pd.read_excel(form_file)
    
    # 'name' 열을 기준으로 두 데이터프레임 병합
    merged_df = pd.merge(data_df, form_df, on='name', suffixes=('_data', '_form'))
    
    # 이메일이 같은 경우 필터링
    matching_df = merged_df[merged_df['email_data'] == merged_df['email_form']]
    
    # 결과 데이터프레임에 필요한 열 선택
    result_df = matching_df[['name', 'email_data']]
    result_df.rename(columns={'email_data': 'email'}, inplace=True)
    
    # 결과를 새로운 엑셀 파일로 저장
    result_df.to_excel(output_file, index=False)

# 파일 경로 설정
data_file = 'data.xlsx'
form_file = 'form.xlsx'
output_file = 'new-data.xlsx'

# 함수 실행
compare_and_save_matching_emails(data_file, form_file, output_file)