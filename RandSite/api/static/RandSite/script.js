function getNewPrediction() {
  fetch('')
    .then(response => {
      if (!response.ok) {
        throw new Error('Ошибка при получении прогноза');
      }
      return response.json();
    })
    .then(data => {
      if (data.error) {
        // Обработка ошибки
        console.error('Ошибка:', data.error);
        alert(data.error);
      } else {
        document.getElementById('prediction').textContent = data.prediction;
      }
    })
    .catch(error => {
      console.error('Ошибка:', error);
      alert('Произошла ошибка при получении прогноза.');
    });
}