import sympy
import math
import time

def compute_radical(n):
    """计算数字的根基 (Radical)"""
    if n <= 1: return 1
    factors = sympy.factorint(n)
    rad = 1
    for p in factors.keys(): rad *= p
    return rad

def run_weapon_a_topology(limit_n):
    """
    武器 A：全局代数自旋破缺扫描
    验证定律：所有 2n-1 为素数的勒让德区间，内部正自旋是否永远比负自旋少 1？
    """
    print("="*60)
    print(f"🌌 [武器 A] 勒让德区间代数自旋破缺定理验证 (n=2 to {limit_n})")
    print("="*60)
    
    prime_p_count = 0
    law_holds_count = 0
    
    start_time = time.time()
    
    for n in range(2, limit_n + 1):
        p = 2*n - 1
        if sympy.isprime(p):
            prime_p_count += 1
            
            start_val = (n-1)**2
            end_val = n**2
            
            # 统计区间 (start_val, end_val) 内部的自旋
            positive_spin = 0
            negative_spin = 0
            
            for x in range(start_val + 1, end_val):
                if x % p == 0:
                    continue # 唯一的 p 的倍数，自旋为 0
                spin = sympy.jacobi_symbol(x, p)
                if spin == 1:
                    positive_spin += 1
                elif spin == -1:
                    negative_spin += 1
            
            # 验证定律：负自旋 - 正自旋 == 1
            if negative_spin - positive_spin == 1:
                law_holds_count += 1
                
    elapsed = time.time() - start_time
    print(f"[*] 扫描完毕！耗时: {elapsed:.2f} 秒")
    print(f"[*] 在 n <= {limit_n} 中，共发现 {prime_p_count} 个满足标尺为素数的靶场。")
    print(f"[*] 绝对定律验证结果: {law_holds_count} / {prime_p_count} (匹配率 {(law_holds_count/prime_p_count)*100:.2f}%)")
    print(f"[*] 物理结论: 大自然在勒让德区间内部，绝对且永久地维持了【负自旋过剩】的拓扑破缺！\n")


def run_weapon_b_wronskian(n_targets):
    """
    武器 B：离散朗斯基体积与 ABC 压缩极限测算
    追踪不同规模 n 下，最长素数真空（全合数序列）的几何压缩率演化。
    """
    print("="*60)
    print("🗜️ [武器 B] 离散朗斯基体积 (ABC 压缩率) 极深空演化演练")
    print("="*60)
    
    print(f"{'n 规模':<12} | {'最长真空 Gap':<12} | {'理论乘积体积 (log)':<20} | {'真实根基体积 (log)':<20} | {'ABC 压缩比率 (q)'}")
    print("-" * 90)
    
    for n in n_targets:
        start_val = (n-1)**2
        end_val = n**2
        
        max_gap_seq = []
        current_gap = []
        
        for x in range(start_val, end_val + 1):
            if not sympy.isprime(x):
                current_gap.append(x)
            else:
                if len(current_gap) > len(max_gap_seq):
                    max_gap_seq = current_gap
                current_gap = []
        if len(current_gap) > len(max_gap_seq):
            max_gap_seq = current_gap
            
        gap_len = len(max_gap_seq)
        
        if gap_len == 0:
            continue
            
        # 计算体积与根基
        total_product_log = 0.0
        # 为了防止大数溢出，我们在计算压缩率时采用对数累加与质因数合并
        global_factors = set()
        for x in max_gap_seq:
            total_product_log += math.log(x)
            factors = sympy.factorint(x)
            for p in factors.keys():
                global_factors.add(p)
                
        total_radical_log = sum(math.log(p) for p in global_factors)
        compression_ratio = total_product_log / total_radical_log if total_radical_log > 0 else 1.0
        
        print(f"{n:<12} | {gap_len:<12} | {total_product_log:<20.2f} | {total_radical_log:<20.2f} | {compression_ratio:.4f}")

if __name__ == '__main__':
    # 1. 武器 A：对前 5000 个区间进行拓扑定律的暴力验证
    run_weapon_a_topology(5000)
    
    # 2. 武器 B：对跨度极大的 n 进行真空压缩率演化测算
    # 从微观的 n=100，一路飙升到深空的 n=200,000 (四百亿空域)
    targets = [100, 500, 1000, 5000, 10000, 50000, 100000, 200000]
    run_weapon_b_wronskian(targets)