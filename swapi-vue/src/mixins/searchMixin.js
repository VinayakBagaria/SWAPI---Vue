export default{
  computed:{
    filteredPeople(){
      return this.people.filter((person) => {
        return person;
      })
    }
  }
}