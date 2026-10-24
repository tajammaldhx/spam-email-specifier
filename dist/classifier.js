(function(root){
function classify(text,m){
 const tokens=text.toLowerCase().match(/[\p{L}\p{N}_]{2,}/gu)||[], counts=new Map();
 for(const t of tokens){if(Object.hasOwn(m.vocabulary,t)){const i=m.vocabulary[t];counts.set(i,(counts.get(i)||0)+1)}}
 let norm=0;for(const [i,c] of counts){let w=c*m.idf[i];counts.set(i,w);norm+=w*w}norm=Math.sqrt(norm);
 const scores=[...m.prior];if(norm)for(const [i,w] of counts){scores[0]+=w/norm*m.logProb[0][i];scores[1]+=w/norm*m.logProb[1][i]}
 const probability=1/(1+Math.exp(scores[0]-scores[1]));return {label:scores[1]>scores[0]?1:0,probability,matched:counts.size};
}root.classify=classify;if(typeof module!=='undefined')module.exports=classify;
})(globalThis);
