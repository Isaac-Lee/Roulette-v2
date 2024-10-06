// 카운트다운 시작 함수
function startCountdown() {
    const countdownElement = document.getElementById('countdown');
    let countdownValue = 5;  // 5초부터 시작
    countdownElement.style.display = 'block';  // 카운트다운 표시
    countdownElement.innerHTML = countdownValue;  // 초기값 표시
    
    // 1초마다 카운트다운 업데이트
    const countdownInterval = setInterval(() => {
        countdownValue -= 1;
        countdownElement.innerHTML = countdownValue;
        
        if (countdownValue === 0) {
            clearInterval(countdownInterval);  // 카운트다운 완료
            countdownElement.style.display = 'none';  // 카운트다운 숨기기
            
            // 추첨 버튼 클릭 시 폼 제출
            document.getElementById('drawForm').submit();
        }
    }, 1000);  // 1000ms = 1초
}
