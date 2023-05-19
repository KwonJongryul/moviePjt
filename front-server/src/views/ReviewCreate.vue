<template>
  <div>
    <form>
      <p>
        <label for="title"><strong>제목</strong></label>
        <input type="text" :v-model="title" id="title">
      </p>
      <p>
        <label for="date"><strong>감상날짜</strong></label>
        <input type="date" :v-model="watch_date" id="date">
      </p>
      <p>
        <label for="vote"><strong>내 평점</strong></label>
        <input type="range" :v-model="watch_date" id="vote" min="0" max="10" step="0.5">
      </p>
      <p>
        <label for="vote"><strong>내용</strong></label><br>
        <textarea cols="30" rows="10" v-model="context"></textarea>
      </p>
      <p>
        <label for="vote"><strong>명대사를 적어주세요!</strong></label><br>
        <input type="text" :v-model="title" id="title">
      </p>
    </form>
  </div>
</template>

<script>
export default {
  name : 'ReviewCreate',
  data () {
    return {
      title : null,
      context : null,
      watch_date : null,
      quotes : null,
      movie : null,
      vote : 0
    }
  }
}
</script>

<style>

</style>