// setup datepicker for help request creation
datepicker('.dp_start', {
  formatter: (input, date, instance) => {
    const value = date.toLocaleDateString('de-DE')
    input.value = value
  }
});
datepicker('.dp_end', {
  formatter: (input, date, instance) => {
    const value = date.toLocaleDateString('de-DE')
    input.value = value
  }
});
