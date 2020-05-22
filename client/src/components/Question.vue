<template>
<!-- eslint-disable max-len -->
  <div>
    <div>
      <div class="container">
        <div  id="navbar-header">
          <img src="../assets/question.png"  width="70px" height="70px" >
          <a id="navbar-name">Song Question Answering</a>
        </div>
      </div>
      <br><br><br><br>
      <h5 id="lefttext">CPE372   Natural  Laguage Processing</h5>
      <br><br><br><br>
      <h3 id="margin">Let’s ask some questions about your interesting songs ! </h3>
      <br><br><br><br>
      <h4 id="margin2">Song Question and Answering is the system that collects all data about English songs.
                <br>Please type something that you interested about song!  We can help you find it.</h4>
      <br>
      <div class="container-fluid bg-1 text-center">
        <div id="search-container" style="color: whitesmoke;">
          <form>
            <input id= "question" type="text" v-model="question">
          </form>
        </div>
        <form @submit="onSubmit" @reset="onReset">
          <button id = "ask" type="submit">Ask</button>
          <button id = "reset" type="reset">Reset</button>
        </form>
        <div id="search-img">
          <img src="../assets/search.png"  width="35px" height="35px">
        </div>
        <div v-if="answer!=null">
          <div id="answer">{{answer}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      question: '',
      answer: null,
    };
  },
  methods: {
    getAnswer() {
      const path = 'http://localhost:5000/qa';
      axios.get(path)
        .then((res) => {
          this.answer = res.data.answer;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    askQuestion(payload) {
      const path = 'http://localhost:5000/qa';
      axios.post(path, payload)
        .then(() => {
          this.getAnswer();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getAnswer();
        });
    },
    initForm() {
      this.question = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        question: this.question, // property shorthand
      };
      this.askQuestion(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.initForm();
    },
  },
  created() {
    this.getAnswer();
  },
};
</script>

<style>
body, html {
  height: 100%;
  margin: 0;
  font-family: Poppins;
}

#question {
  color: #7173C5;
  font-style: normal;
  top: 150px;
  font-weight: normal;
  font-family: 'Poppins', sans-serif;
  text-align: center;
  font-size: 20px;
  border-radius: 70px;
  border: 0px;
  padding: 25px;
  float: center;
  background: #FFFFFF;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.08);
  width: 890px;
  height: 70px;
}
#search-container {
  float: center;
  left: 220px;
  position: absolute;
}
#ask {
  float: center;
  color: #F9F3EC;
  text-align: center;
  top:410px;
  position: absolute;
  font-family: 'Poppins', sans-serif;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 27px;
  background: rgba(104, 102, 200, 0.7);
  border: 3px solid #7173C5;
  border-radius: 20px;
  padding-top:0px;
  cursor: pointer;
  width: 115px;
  height: 35px;
  left: 535px;
}
#ask:hover {
  background: #7173C5;
  text-shadow: salmon;
}
#reset {
  float: center;
  color: rgba(104, 102, 200, 0.8);
  float: center;
  top:408px;
  position: absolute;
  text-align: center;
  position: absolute;
  font-family: 'Poppins', sans-serif;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 27px;
  background: #F9F3EC;
  border: 3px solid #F5EEF8;
  border-radius: 20px;
  cursor: pointer;
  width: 115px;
  height: 40px;
  left: 665px;
}
#reset:hover {
  background  : #eee0ff;
}
#answer {
  float: center;
  color: #7173C5;
  position: absolute;
  font-weight: 500;
  font-size: 24px;
  text-align: center;
  font-family: 'Poppins', sans-serif;
  background: rgba(210, 209, 236, 0.18);
  border: 2px solid rgba(104, 102, 200, 0.28);
  border-radius: 30px;
  font-size: 20px;
  width: 740px;
  height: 280px;
  padding: 30px;
  margin-top: 95px;
  margin-left: 285px;
}
#navbar-header {
    position: absolute;
    width: 72px;
    height: 71px;
    left: 60px;
    top: 30px;
}

#navbar-name {
    /* Song Question Answering */
    position: absolute;
    width: 314px;
    left: 90px;
    margin-top:15px;
    font-family: 'Poppins', sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 24px;
    line-height: 36px;
    color: #545772;
    }
#lefttext {
    top: 55px;
    right: 40px;
    position: absolute;
    font-family: 'Poppins', sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 14px;
    color: #545772;
  }


#margin {
    position: absolute;
    width: 669px;
    height: 36px;
    left: 340px; /*378*/
    top:180px;
    font-family: 'Poppins', sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 24px;
    line-height: 36px;
    text-align: center;
    color: rgba(104, 102, 200, 0.8);
    }
#margin2 {
    position: absolute;
    top:230px;
    font-family: 'Poppins', sans-serif;
    left: 285px;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 27px;
    text-align: center;
    color: #5F5F5F;
  }
#search-img {
  /* ion:search */
  position: absolute;
  left: 250px; /*316*/
  top:330px;
}
</style>
