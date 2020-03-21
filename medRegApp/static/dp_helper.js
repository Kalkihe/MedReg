// setup datepicker for helper registration
datepicker('.mld', {
  formatter: (input, date, instance) => {
    const value = date.toLocaleDateString('de-DE')
    input.value = value
  }
});
